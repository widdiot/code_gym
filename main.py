import argparse
from pathlib import Path

from src.io_utils import load_problems_from_csv
from src.planning import SimplePlanner, Tracker
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Code Gym Session Planner")
    parser.add_argument("--items", required=True, help="Path to cg_items.csv")
    parser.add_argument("--subs", required=True, help="Path to cg_submissions.csv")
    parser.add_argument("--tracker", default="tracker.csv", help="Path to tracker.csv")
    parser.add_argument("--logs", default="logs.csv", help="Path to logs.csv")
    parser.add_argument("--minutes", type=int, default=60, help="Total minutes for session")
    parser.add_argument("--daytype", choices=["weekday", "weekend"], default="weekday")
    parser.add_argument("--categories", nargs="*", default=None, help="List of categories to include (space separated, e.g. --categories arrays dp)")
    parser.add_argument("--categories_file", type=str, default=None, help="Path to a file with categories to include, one per line.")
    parser.add_argument("--interactive", action="store_true", help="Prompt for logs and update tracker/logs")
    parser.add_argument("--dev", action="store_true", help="Dev mode: write to *.dev.csv")
    args = parser.parse_args()

    items_csv = Path(args.items).expanduser().resolve()
    subs_csv = Path(args.subs).expanduser().resolve()

    problems_dict = load_problems_from_csv(items_csv, subs_csv)
    problems = list(problems_dict.values())
    categories_set = set()
    if args.categories_file:
        with open(args.categories_file, "r", encoding="utf-8") as f:
            categories_set = set(line.strip().lower() for line in f if line.strip())
    elif args.categories:
        categories_set = set([c.lower() for c in args.categories])
    if categories_set:
        filtered_problems = []
        for p in problems:
            if p.category:
                for cat in p.category.lower().split('/'):
                    if cat.strip().lower() in categories_set:
                        filtered_problems.append(p)
                        break
        problems = filtered_problems
    tracker = Tracker()  # Empty tracker for now; extend as needed
    reference_date = datetime.now()
    planner = SimplePlanner(problems, tracker, reference_date)
    plan = planner.generate_plan()

    # Limit plan to minutes//10 problems: 2 easy, rest medium, all due, sorted by need score
    max_problems = max(1, args.minutes // 10)
    easy = [item for item in plan if (item.problem.difficulty or '').lower() == 'easy']
    medium = [item for item in plan if (item.problem.difficulty or '').lower() == 'medium']
    selected = easy[:2] + medium[:max_problems-2] if max_problems > 2 else easy[:max_problems]
    # If not enough easy/medium, fill with other problems
    if len(selected) < max_problems:
        others = [item for item in plan if item not in selected]
        selected += others[:max_problems - len(selected)]

    print(f"\nSimple Plan (max {max_problems} problems, 2 easy + rest medium):")
    for i, item in enumerate(selected, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()