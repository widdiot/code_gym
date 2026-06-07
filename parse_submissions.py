import json
from pathlib import Path
from datetime import datetime
from src.parsing import parse_problem_dir_name, parse_problem_difficulty, parse_submission_filename

def main(export_dir, out_file):
    export_dir = Path(export_dir)
    out_file = Path(out_file)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    submissions_rows = []

    if not export_dir.exists():
        print(f"Error: Export directory '{export_dir}' does not exist.")
        return

    for problem_dir in sorted(export_dir.iterdir()):
        if not problem_dir.is_dir():
            continue
        # Skip hidden directories
        if problem_dir.name.startswith("."):
            continue

        qid, slug = parse_problem_dir_name(problem_dir.name)
        if not qid:
            continue

        md_file = next(problem_dir.glob("*.md"), None)
        difficulty = parse_problem_difficulty(md_file) if md_file else None

        for sub_file in problem_dir.glob("*.py"):
            meta = parse_submission_filename(sub_file.name)
            if not meta:
                continue

            row = {
                "question_id": qid,
                "title_slug": slug,
                "difficulty": difficulty,
                "status": meta["status"],
                "runtime": meta["runtime"],
                "memory": meta["memory"],
                "submitted_at": meta["submitted_at"],
                "file_path": str(sub_file),
                "problem_dir": problem_dir.name,
            }
            submissions_rows.append(row)

    # Sort submissions chronologically for consistency
    submissions_rows.sort(key=lambda x: x["submitted_at"])

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(submissions_rows, f, indent=2)

    print(f"Successfully parsed {len(submissions_rows)} submissions into {out_file}")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="Parse LeetCode export submissions to a JSON file.")
    ap.add_argument("--export_dir", default="./submissions", help="Path to submissions directory")
    ap.add_argument("--out_file", default="out/cg_submissions.json", help="Path to output JSON file")
    args = ap.parse_args()
    main(args.export_dir, args.out_file)
