from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class Submission:
    """Represents a single solution attempt for a problem.
    """
    problem: str
    submitted_at: datetime
    status: str
    runtime: str
    memory: str
    file_path: str

@dataclass
class Problem:
    """A coding problem with a collection of submissions.
    """
    question_id: str
    title_slug: str
    difficulty: Optional[str] = None
    submissions: List[Submission] = field(default_factory=list)

    def add_submission(self, submission: Submission) -> None:
        self.submissions.append(submission)

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
