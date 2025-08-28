
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from .parsing import parse_runtime, parse_memory


@dataclass
class Submission:
    """Represents a single solution attempt for a problem.

    The `submitted_at` field stores an aware datetime (UTC).  Runtime and
    memory strings are stored verbatim and parsed lazily when queried for
    numeric values.  The `status` is expected to match the LeetCode display,
    e.g. 'Accepted', 'Wrong Answer', 'Time Limit Exceeded'.
    """
    problem: str
    submitted_at: datetime
    status: str
    runtime: str
    memory: str
    file_path: str

    def runtime_ms(self) -> Optional[float]:
        return parse_runtime(self.runtime)

    def memory_mb(self) -> Optional[float]:
        return parse_memory(self.memory)



@dataclass
class Problem:
    """A coding problem with a collection of submissions.

    `question_id` uniquely identifies the problem (string or int).  The
    `difficulty` may be 'Easy', 'Medium' or 'Hard'.  Submissions are stored
    chronologically when added through `add_submission` but the class does
    not require ordering.
    """

    question_id: str
    title_slug: str
    difficulty: Optional[str] = None
    category: Optional[str] = None
    submissions: List[Submission] = field(default_factory=list)

    def add_submission(self, submission: Submission) -> None:
        self.submissions.append(submission)

    # Derived properties ------------------------------------------------------
    def total_submissions(self) -> int:
        return len(self.submissions)

    def accepted_submissions(self) -> int:
        return sum(1 for s in self.submissions if s.status.lower() == "accepted")

    def last_submission(self) -> Optional[Submission]:
        if not self.submissions:
            return None
        return max(self.submissions, key=lambda s: s.submitted_at)

    def last_status(self) -> Optional[str]:
        last = self.last_submission()
        return last.status if last else None

    def last_submission_at(self) -> Optional[datetime]:
        last = self.last_submission()
        return last.submitted_at if last else None

    def age_days(self, reference_date: datetime) -> Optional[int]:
        """Return the number of days since the last submission.

        If there are no submissions then return None.
        """
        last = self.last_submission_at()
        if last is None:
            return None
        # difference in days; round down.
        return max(0, (reference_date.date() - last.date()).days)

    def last_accepted_submission(self) -> Optional[Submission]:
        accepted = [s for s in self.submissions if s.status.lower() == "accepted"]
        if not accepted:
            return None
        return max(accepted, key=lambda s: s.submitted_at)

    def best_runtime(self) -> Optional[float]:
        """Return the smallest runtime among accepted submissions (ms)."""
        best = None
        for s in self.submissions:
            if s.status.lower() == "accepted":
                ms = s.runtime_ms()
                if ms is not None:
                    if best is None or ms < best:
                        best = ms
        return best

    def best_memory(self) -> Optional[float]:
        """Return the smallest memory usage among accepted submissions (MB)."""
        best = None
        for s in self.submissions:
            if s.status.lower() == "accepted":
                mem = s.memory_mb()
                if mem is not None:
                    if best is None or mem < best:
                        best = mem
        return best

    def last_accepted_runtime(self) -> Optional[float]:
        last = self.last_accepted_submission()
        return last.runtime_ms() if last else None

    def last_accepted_memory(self) -> Optional[float]:
        last = self.last_accepted_submission()
        return last.memory_mb() if last else None

    def recent_accuracy(self, k: int = 5) -> Optional[float]:
        """Return the ratio of accepted submissions in the last k submissions.

        If there are fewer than k submissions the ratio is computed over
        whatever is available.  Returns None if there are no submissions.
        """
        if not self.submissions:
            return None
        # Sort by submission time ascending
        sorted_subs = sorted(self.submissions, key=lambda s: s.submitted_at, reverse=True)
        recent = sorted_subs[:k]
        accepted = sum(1 for s in recent if s.status.lower() == "accepted")
        return accepted / len(recent) if recent else 0.0

    def optimality_gap(self) -> bool:
        """True if the latest accepted submission is ≥30% worse than the best.

        Compares both runtime and memory.  If either runtime or memory
        difference exceeds 30% then returns True.  Only considered when
        there are at least two accepted submissions.
        """
        # TODO optimality gap can also be obtained from the tracker
        best_rt = self.best_runtime()
        best_mem = self.best_memory()
        last_rt = self.last_accepted_runtime()
        last_mem = self.last_accepted_memory()
        # Need at least two accepted submissions for a meaningful comparison
        if best_rt is None or best_mem is None or last_rt is None or last_mem is None:
            return False
        # If there's only one accepted submission then best_rt == last_rt.
        if self.accepted_submissions() <= 1:
            return False
        gap_rt = last_rt - best_rt if best_rt is not None else 0
        gap_mem = last_mem - best_mem if best_mem is not None else 0
        # 30% relative difference: gap / best > 0.3
        if best_rt and gap_rt / best_rt > 0.3:
            return True
        if best_mem and gap_mem / best_mem > 0.3:
            return True
        return False

    def compute_stats(self):
        total = self.total_submissions()
        accepted = self.accepted_submissions()
        first = min(self.submissions, key=lambda s: s.submitted_at, default=None)
        last = max(self.submissions, key=lambda s: s.submitted_at, default=None)
        return {
            "total_submissions": total,
            "accepted_submissions": accepted,
            "first_submission_at": first.submitted_at if first else None,
            "last_submission_at": last.submitted_at if last else None,
            "last_status": last.status if last else None,
        }

# class Problem:
#     def __init__(self, question_id, title_slug, difficulty=None):
#         self.question_id = question_id
#         self.title_slug = title_slug
#         self.difficulty = difficulty
#         self.submissions = []
    
#     def __str__(self):
#         return f"Problem({self.question_id}, {self.title_slug}, submissions={len(self.submissions)})"

#     def __repr__(self):
#         return self.__str__()

#     def add_submission(self, submission):
#         self.submissions.append(submission)

#     def compute_stats(self):
#         total = len(self.submissions)
#         accepted = sum(1 for s in self.submissions if s.status.lower() == "accepted")
#         first = min(self.submissions, key=lambda s: s.submitted_at, default=None)
#         last = max(self.submissions, key=lambda s: s.submitted_at, default=None)
#         return {
#             "total_submissions": total,
#             "accepted_submissions": accepted,
#             "first_submission_at": first.submitted_at if first else None,
#             "last_submission_at": last.submitted_at if last else None,
#             "last_status": last.status if last else None,
#         }

# class Submission:
#     def __init__(self, problem, submitted_at, status, runtime, memory, file_path):
#         self.problem = problem
#         self.submitted_at = submitted_at
#         self.status = status
#         self.runtime = runtime
#         self.memory = memory
#         self.file_path = file_path