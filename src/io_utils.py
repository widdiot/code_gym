
import csv
from pathlib import Path
from typing import Dict
from .core import Problem, Submission
from datetime import datetime

DATETIME_FMT = "%Y-%m-%d %H:%M:%S"

def write_csv(rows, out_path):
    if not rows:
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            f.write("")
        return
    cols = list(rows[0].keys())
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)

def load_problems_from_csv(items_csv: Path, subs_csv: Path) -> Dict[str, Problem]:
    # Build problems from items first
    items = []
    with open(items_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            items.append(r)

    problems: Dict[str, Problem] = {}
    for it in items:
        qid = (it.get("question_id") or "").strip() or None
        slug = (it.get("title_slug") or "").strip() or None
        title = it.get("title") or None
        difficulty = it.get("difficulty") or None
        category = it.get("category")

        prob = Problem(qid, slug, difficulty=difficulty, category=category)
        # Use question_id as the common key
        problems[qid] = prob

    # Add submissions
    with open(subs_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            qid = (r.get("question_id") or "").strip() or None
            slug = (r.get("title_slug") or "").strip() or None
            # Use question_id as the common key
            key_id = qid
            if key_id not in problems:
                # create on the fly
                problems[key_id] = Problem(qid, slug, difficulty=r.get("difficulty") or None)
            submitted_at_str = r.get("submitted_at") or ""

            dt = datetime.strptime(submitted_at_str, DATETIME_FMT)
            sub = Submission(
                problem=problems[key_id],
                submitted_at=dt,
                status=(r.get("status") or "").strip(),
                runtime=r.get("runtime"),
                memory=r.get("memory"),
                file_path=r.get("file_path"),
            )
            problems[key_id].add_submission(sub)

    return problems