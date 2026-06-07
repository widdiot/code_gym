from dataclasses import dataclass
from datetime import date, timedelta
from typing import Dict, List, Optional
from .core import Problem

BOX_INTERVALS = {
    "L1": 1,
    "L2": 3,
    "L3": 7,
    "L4": 15,
    "L5": 30,
    "L6": 60
}

def promote(box: str) -> str:
    order = ["L1", "L2", "L3", "L4", "L5", "L6"]
    try:
        idx = order.index(box)
        if idx < len(order) - 1:
            return order[idx + 1]
    except ValueError:
        pass
    return box

@dataclass
class LeitnerState:
    box: str
    next_due: date
    last_attempt_date: date
    last_attempt_status: str
    days_overdue: int

class LeitnerScheduler:
    def __init__(self, problems: List[Problem], limit_days: int = 30) -> None:
        self.problems = problems
        self.limit_days = limit_days

    def simulate_leitner(self, problem: Problem, today: date) -> Optional[LeitnerState]:
        """Simulate chronological Leitner boxes based on submissions within the active run window.
        """
        if not problem.submissions:
            return None

        # Filter submissions to only those within the active run window (last N days)
        limit_date = today - timedelta(days=self.limit_days)
        run_subs = [
            s for s in problem.submissions 
            if s.submitted_at.date() >= limit_date
        ]

        if not run_subs:
            return None

        # Sort submissions chronologically
        sorted_subs = sorted(run_subs, key=lambda s: s.submitted_at)
        
        # Group submissions by calendar date
        daily_submissions: Dict[date, List[str]] = {}
        for sub in sorted_subs:
            d = sub.submitted_at.date()
            if d not in daily_submissions:
                daily_submissions[d] = []
            daily_submissions[d].append(sub.status)

        sorted_dates = sorted(daily_submissions.keys())
        
        # State machine variables
        box = "L1"
        next_due = sorted_dates[0]  # dummy initial value

        # Process each date chronologically
        for i, d in enumerate(sorted_dates):
            statuses = daily_submissions[d]
            passed = any(status.lower() == "accepted" for status in statuses)

            if i == 0:
                # First day with submissions in the active run
                if passed:
                    box = "L2"
                    next_due = d + timedelta(days=BOX_INTERVALS["L2"])
                else:
                    box = "L1"
                    next_due = d + timedelta(days=BOX_INTERVALS["L1"])
            else:
                # Subsequent days with attempts
                if passed:
                    if d >= next_due:
                        box = promote(box)
                    # if solved early, box is kept (no promotion)
                    next_due = d + timedelta(days=BOX_INTERVALS[box])
                else:
                    # any failure on this day resets to L1
                    box = "L1"
                    next_due = d + timedelta(days=BOX_INTERVALS["L1"])

        # Determine last attempt date and status
        last_sub = sorted_subs[-1]
        last_attempt_date = last_sub.submitted_at.date()
        last_attempt_status = last_sub.status

        return LeitnerState(
            box=box,
            next_due=next_due,
            last_attempt_date=last_attempt_date,
            last_attempt_status=last_attempt_status,
            days_overdue=0  # set dynamically relative to today
        )

    def get_due_problems(self, today: date) -> List[dict]:
        """Filter problems by limit_days, simulate Leitner states, and return due problems.
        """
        due_list = []
        for p in self.problems:
            if not p.submissions:
                continue
            
            # Find the most recent submission date
            latest_sub = max(p.submissions, key=lambda s: s.submitted_at)
            latest_date = latest_sub.submitted_at.date()
            
            # Filter by limit_days (active run constraint)
            if (today - latest_date).days > self.limit_days:
                continue

            state = self.simulate_leitner(p, today)
            if not state:
                continue

            # Check if due (next_due is today or in the past)
            if state.next_due <= today:
                state.days_overdue = (today - state.next_due).days
                due_list.append({
                    "problem": p,
                    "state": state
                })

        # Sort: smaller boxes first (higher revision priority), then most overdue
        due_list.sort(key=lambda item: (item["state"].box, -item["state"].days_overdue))
        return due_list

    def get_upcoming_problems(self, today: date) -> List[dict]:
        """Filter problems by limit_days, simulate Leitner states, and return upcoming (not due) problems.
        """
        upcoming_list = []
        for p in self.problems:
            if not p.submissions:
                continue
            
            # Find the most recent submission date
            latest_sub = max(p.submissions, key=lambda s: s.submitted_at)
            latest_date = latest_sub.submitted_at.date()
            
            # Filter by limit_days (active run constraint)
            if (today - latest_date).days > self.limit_days:
                continue

            state = self.simulate_leitner(p, today)
            if not state:
                continue

            # Check if upcoming (next_due is in the future)
            if state.next_due > today:
                upcoming_list.append({
                    "problem": p,
                    "state": state
                })

        # Sort: next_due date ascending (soonest due first), then box size
        upcoming_list.sort(key=lambda item: (item["state"].next_due, item["state"].box))
        return upcoming_list
