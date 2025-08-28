import math
from datetime import datetime
from typing import Optional
from .core import Problem


# Assuming Problem is defined elsewhere and imported here
# from .problem import Problem
class NeedScore:
    """Compute a composite need-to-revise score for a problem.

    The score is composed of several additive components:

    - **Recency (0-40):** Older problems get larger contribution.  Scales
      logarithmically: recency = 40 * log1p(age_days) / log1p(60) where
      age_days is days since last submission.
    - **Struggle (0-30):** Number of total submissions times six, capped at 30.
    - **Difficulty (0-15):** +10 for Medium, +15 for Hard; 0 for Easy or unknown.
    - **Status penalty (0-20):** +20 if the last status is not 'Accepted'.
    - **Recent accuracy penalty (0-15):** +10 if fewer than 60% of last 5
      submissions were accepted, or +15 if fewer than 40%.
    - **Optimality nudge (+8):** added if the latest accepted run or memory is
      ≥30% worse than the best accepted.

    The final `score` attribute is the sum of these components.  Higher
    scores indicate a higher priority for revision.
    """

    def __init__(self, problem: Problem, reference_date: datetime) -> None:
        self.problem = problem
        self.reference_date = reference_date
        self.recency_score = self._compute_recency()
        self.struggle_score = self._compute_struggle()
        self.difficulty_score = self._compute_difficulty()
        self.status_penalty = self._compute_status_penalty()
        self.accuracy_penalty = self._compute_accuracy_penalty()
        self.optimality_nudge = 8 if problem.optimality_gap() else 0
        self.total_score = (
            self.recency_score
            + self.struggle_score
            + self.difficulty_score
            + self.status_penalty
            + self.accuracy_penalty
            + self.optimality_nudge
        )

    def _compute_recency(self) -> float:
        days = self.problem.age_days(self.reference_date)
        if days is None:
            return 0.0
        # log1p scaling up to ~40 at 60 days
        return 40.0 * math.log1p(days) / math.log1p(60.0)

    def _compute_struggle(self) -> float:
        return min(30.0, 6.0 * self.problem.total_submissions())

    def _compute_difficulty(self) -> float:
        diff = (self.problem.difficulty or "").lower()
        if diff == "medium":
            return 10.0
        if diff == "hard":
            return 15.0
        return 0.0

    def _compute_status_penalty(self) -> float:
        last_status = (self.problem.last_status() or "").lower()
        # Consider only the first word; WA/TLE/RTE/CE all have first word
        if last_status == "accepted":
            return 0.0
        if not last_status:
            return 20.0
        if last_status.startswith("wrong") or last_status.startswith("time") or last_status.startswith("runtime") or last_status.startswith("compile") or last_status.startswith("memory"):
            return 20.0
        # Unknown statuses like 'Partial' get a penalty too
        return 20.0

    def _compute_accuracy_penalty(self) -> float:
        acc = self.problem.recent_accuracy(k=5)
        if acc is None:
            return 0.0
        if acc < 0.4:
            return 15.0
        if acc < 0.6:
            return 10.0
        return 0.0

    def explain(self) -> str:
        parts = []
        if self.recency_score:
            days = self.problem.age_days(self.reference_date) or 0
            parts.append(f"recency {self.recency_score:.1f} (last touched {days}d ago)")
        if self.struggle_score:
            parts.append(f"struggle {self.struggle_score:.1f} ({self.problem.total_submissions()} submissions)")
        if self.difficulty_score:
            diff_label = self.problem.difficulty or "unknown"
            parts.append(f"difficulty {self.difficulty_score:.1f} ({diff_label})")
        if self.status_penalty:
            last_status = self.problem.last_status() or "None"
            parts.append(f"status {self.status_penalty:.1f} (last={last_status})")
        if self.accuracy_penalty:
            acc = self.problem.recent_accuracy(k=5)
            if acc is not None:
                parts.append(f"accuracy {self.accuracy_penalty:.1f} (recent {acc*100:.0f}%)")
        if self.optimality_nudge:
            parts.append(f"opt_gap {self.optimality_nudge:.1f}")
        parts.append(f" => need={self.total_score:.1f}")
        return " + ".join(parts)

    @property
    def score(self) -> float:
        return self.total_score