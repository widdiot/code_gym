
import csv
from pathlib import Path
from datetime import datetime
from src.parsing import parse_problem_dir_name, parse_problem_difficulty, parse_submission_filename
from src.core import Problem, Submission
from src.io_utils import write_csv


def main(export_dir, out_dir):
    export_dir = Path(export_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    problems = {}
    submissions_rows = []

    for problem_dir in sorted(export_dir.iterdir()):
        if not problem_dir.is_dir():
            continue
        qid, slug = parse_problem_dir_name(problem_dir.name)
        md_file = next(problem_dir.glob("*.md"), None)
        difficulty = parse_problem_difficulty(md_file) if md_file else None

        key = f"{qid}-{slug}"
        if key not in problems:
            problems[key] = Problem(qid, slug, difficulty=difficulty)

        problem = problems[key]

        for sub_file in problem_dir.glob("*.py"):
            meta = parse_submission_filename(sub_file.name)
            if not meta:
                continue
            try:
                submission_dt = datetime.strptime(meta["submitted_at"], "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue

            submission = Submission(
                problem=problem,
                submitted_at=submission_dt,
                status=meta["status"],
                runtime=meta["runtime"],
                memory=meta["memory"],
                file_path=str(sub_file)
            )
            problem.add_submission(submission)

            row = {
                "question_id": qid,
                "title_slug": slug,
                "lang": "python3",
                "status": meta["status"],
                "runtime": meta["runtime"],
                "memory": meta["memory"],
                "submitted_at": meta["submitted_at"],
                "file_path": str(sub_file),
                "problem_dir": problem_dir.name,
            }
            submissions_rows.append(row)

    items_map = {}
    for key, problem in problems.items():
        stats = problem.compute_stats()
        items_map[key] = {
            "question_id": problem.question_id,
            "title_slug": problem.title_slug,
            "difficulty": problem.difficulty,
            "total_submissions": stats["total_submissions"],
            "accepted_submissions": stats["accepted_submissions"],
            "first_submission_at": stats["first_submission_at"],
            "last_submission_at": stats["last_submission_at"],
            "last_status": stats["last_status"],
        }

    write_csv(submissions_rows, out_dir / "cg_submissions.csv")
    write_csv(list(items_map.values()), out_dir / "cg_items.csv")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--export_dir", required=True)
    ap.add_argument("--out_dir", default=".")
    args = ap.parse_args()
    main(args.export_dir, args.out_dir)
