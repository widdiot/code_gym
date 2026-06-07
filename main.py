import argparse
from pathlib import Path
from datetime import date, datetime
from src.io_utils import load_problems_from_json
from src.planning import LeitnerScheduler

def print_methodology():
    print("\n" + "=" * 60)
    print("METHODOLOGY & USAGE INSTRUCTIONS:")
    print("=" * 60)
    print("1. CHECK DUE: Run 'python3 main.py' to see what questions are due today.")
    print("2. SOLVE: Go to LeetCode, solve, and submit the due questions.")
    print("3. SYNC SUBMISSIONS: Run './dump_leetcode.sh .cookies' to pull new submissions.")
    print("4. PARSE: Run 'python3 parse_submissions.py' to compile into the JSON database.")
    print("5. VERIFY: Run 'python3 main.py' again. The solved questions are now promoted")
    print("   and will disappear from the due list.")
    print("-" * 60)
    print("Note: The tool is completely stateless. It calculates states dynamically")
    print("      from your full submission history. Delayed syncs are handled automatically.")
    print("=" * 60 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Code Gym - Automated Spaced-Repetition Daily Reminder CLI")
    parser.add_argument("--subs", default="out/cg_submissions.json", help="Path to cg_submissions.json")
    parser.add_argument("--limit-days", type=int, default=30, help="Only include questions attempted in the last N days (default: 30)")
    parser.add_argument("--difficulty", choices=["Easy", "Medium", "Hard"], help="Filter due problems by difficulty")
    args = parser.parse_args()

    subs_json = Path(args.subs).expanduser().resolve()
    if not subs_json.exists():
        print(f"Error: JSON database file '{subs_json}' not found.")
        print("Please run 'python3 parse_submissions.py' first to parse your submissions.")
        return

    problems_dict = load_problems_from_json(subs_json)
    problems = list(problems_dict.values())

    today = date.today()
    scheduler = LeitnerScheduler(problems, limit_days=args.limit_days)
    
    # Calculate active problems count
    active_count = 0
    for p in problems:
        if p.submissions:
            latest_sub = max(p.submissions, key=lambda s: s.submitted_at)
            latest_date = latest_sub.submitted_at.date()
            if (today - latest_date).days <= args.limit_days:
                active_count += 1

    due_items = scheduler.get_due_problems(today)
    upcoming_items = scheduler.get_upcoming_problems(today)

    # Filter by difficulty if requested
    if args.difficulty:
        due_items = [
            item for item in due_items 
            if (item["problem"].difficulty or "").lower() == args.difficulty.lower()
        ]
        upcoming_items = [
            item for item in upcoming_items
            if (item["problem"].difficulty or "").lower() == args.difficulty.lower()
        ]

    print("\n" + "=" * 60)
    print("CODE GYM SPACED-REPETITION REMINDER")
    print("=" * 60)
    print(f"Total problems in history: {len(problems)}")
    print(f"Active run problems (last {args.limit_days} days): {active_count}")
    print(f"Due problems today: {len(due_items)}")
    print("=" * 60)

    if due_items:
        print(f"\n{'#':<3} {'ID':<6} {'Title (Difficulty)':<45} {'Box':<5} {'Overdue':<12} {'Last Attempt'}")
        print("-" * 105)
        for i, item in enumerate(due_items, 1):
            prob = item["problem"]
            state = item["state"]
            
            title = prob.title_slug.replace("-", " ").title()
            diff_label = f"({prob.difficulty})" if prob.difficulty else ""
            title_with_diff = f"{title} {diff_label}"
            if len(title_with_diff) > 43:
                title_with_diff = title_with_diff[:40] + "..."

            overdue_txt = "due today" if state.days_overdue == 0 else f"{state.days_overdue} days"
            
            days_since_last = (today - state.last_attempt_date).days
            last_txt = f"{state.last_attempt_status} ({days_since_last} days ago)"

            print(f"{i:<3} {prob.question_id:<6} {title_with_diff:<45} {state.box:<5} {overdue_txt:<12} {last_txt}")
        print("-" * 105)
    else:
        print("\n🎉 No problems are due today! Keep up the good work.")

    if upcoming_items:
        print(f"\nUPCOMING PROBLEMS (Not Due Yet):")
        print(f"{'#':<3} {'ID':<6} {'Title (Difficulty)':<45} {'Box':<5} {'Due In':<12} {'Last Attempt'}")
        print("-" * 105)
        for i, item in enumerate(upcoming_items, 1):
            prob = item["problem"]
            state = item["state"]
            
            title = prob.title_slug.replace("-", " ").title()
            diff_label = f"({prob.difficulty})" if prob.difficulty else ""
            title_with_diff = f"{title} {diff_label}"
            if len(title_with_diff) > 43:
                title_with_diff = title_with_diff[:40] + "..."

            days_until = (state.next_due - today).days
            due_in_txt = "tomorrow" if days_until == 1 else f"{days_until} days"
            
            days_since_last = (today - state.last_attempt_date).days
            last_txt = f"{state.last_attempt_status} ({days_since_last} days ago)"

            print(f"{i:<3} {prob.question_id:<6} {title_with_diff:<45} {state.box:<5} {due_in_txt:<12} {last_txt}")
        print("-" * 105)

    print_methodology()

if __name__ == "__main__":
    main()