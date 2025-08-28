from dataclasses import dataclass
from datetime import date, datetime
from typing import Dict, List, Optional
from .core import Problem
from .scoring import NeedScore

# Assuming Problem and NeedScore are defined elsewhere and imported here

@dataclass
class TrackerRow:
    """Simple tracker row used for tests.

    In the full system this would include other fields like invariant notes, but
    here we only record the spaced‑repetition box and the next due date.
    """
    id: str
    box: str
    next_due: date


class Tracker:
    """A minimal tracker for tests.

    A real implementation would load from and save to CSV.  Here we keep it
    simple: the tracker is a mapping from problem id to TrackerRow.  When
    computing due problems the planner will ignore entries that are not due.
    """

    def __init__(self, rows: Optional[Dict[str, TrackerRow]] = None) -> None:
        self.rows: Dict[str, TrackerRow] = rows or {}

    def is_due(self, problem_id: str, reference_date: date) -> bool:
        row = self.rows.get(problem_id)
        if not row:
            # If we don't know the problem just treat it as due
            return True
        return row.next_due <= reference_date


@dataclass
class PlanItem:
    """Represents a planned study item with its technique and rationale."""
    problem: Problem
    need_score: NeedScore

    def __str__(self) -> str:
        return f"{self.problem.question_id} {self.problem.title_slug} ({self.problem.difficulty}) → {self.need_score.total_score:.1f}: {self.need_score.explain()}"


class SimplePlanner:
    """Generate a sorted list of problems to study based on need score.

    The planner filters out any problems that are not due according to the
    supplied tracker.  It then computes a `NeedScore` for each remaining
    problem using the provided reference date and returns a list of
    `PlanItem` objects sorted by descending need score.
    """

    def __init__(self, problems: List[Problem], tracker: Tracker, reference_date: datetime) -> None:
        self.problems = problems
        self.tracker = tracker
        self.reference_date = reference_date

    def generate_plan(self) -> List[PlanItem]:
        due_problems: List[PlanItem] = []
        for p in self.problems:
            if self.tracker.is_due(p.question_id, self.reference_date.date()):
                ns = NeedScore(p, self.reference_date)
                due_problems.append(PlanItem(problem=p, need_score=ns))
        # sort high to low need score
        due_problems.sort(key=lambda item: item.need_score.score, reverse=True)
        return due_problems
