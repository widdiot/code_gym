import json
from pathlib import Path
from typing import Dict
from .core import Problem, Submission
from datetime import datetime

DATETIME_FMT = "%Y-%m-%d %H:%M:%S"

def load_problems_from_json(json_path: Path) -> Dict[str, Problem]:
    """Load problems and all their submissions from a single JSON database.
    """
    if not json_path.exists():
        return {}

    with open(json_path, "r", encoding="utf-8") as f:
        try:
            submissions_data = json.load(f)
        except json.JSONDecodeError:
            return {}

    problems: Dict[str, Problem] = {}
    for entry in submissions_data:
        qid = (entry.get("question_id") or "").strip()
        if not qid:
            continue
        slug = (entry.get("title_slug") or "").strip()
        difficulty = entry.get("difficulty") or None

        if qid not in problems:
            problems[qid] = Problem(qid, slug, difficulty=difficulty)
        else:
            # Update difficulty/slug if missing
            if not problems[qid].difficulty and difficulty:
                problems[qid].difficulty = difficulty
            if not problems[qid].title_slug and slug:
                problems[qid].title_slug = slug

        submitted_at_str = entry.get("submitted_at") or ""
        try:
            dt = datetime.strptime(submitted_at_str, DATETIME_FMT)
        except ValueError:
            continue

        sub = Submission(
            problem=problems[qid],
            submitted_at=dt,
            status=(entry.get("status") or "").strip(),
            runtime=entry.get("runtime") or "",
            memory=entry.get("memory") or "",
            file_path=entry.get("file_path") or ""
        )
        problems[qid].add_submission(sub)

    return problems