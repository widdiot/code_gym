from datetime import datetime, date, timedelta
import unittest

from src.core import Problem, Submission
from src.planning import LeitnerScheduler, promote

class TestLeitnerScheduler(unittest.TestCase):
    def test_promote_helper(self):
        self.assertEqual(promote("L1"), "L2")
        self.assertEqual(promote("L2"), "L3")
        self.assertEqual(promote("L5"), "L6")
        self.assertEqual(promote("L6"), "L6")
        self.assertEqual(promote("Invalid"), "Invalid")

    def test_first_attempt_passed_starts_in_l2(self):
        """A problem with a single Accepted submission on the first day should start in box L2 (3-day interval).
        """
        problem = Problem(question_id="p1", title_slug="p1", difficulty="Easy")
        # Submitted on 2025-08-28
        sub = Submission(
            problem=problem,
            submitted_at=datetime(2025, 8, 28, 10, 0, 0),
            status="Accepted",
            runtime="10ms",
            memory="10MB",
            file_path=""
        )
        problem.add_submission(sub)

        scheduler = LeitnerScheduler([problem], limit_days=30)
        state = scheduler.simulate_leitner(problem, date(2025, 8, 28))
        self.assertIsNotNone(state)
        self.assertEqual(state.box, "L2")
        self.assertEqual(state.next_due, date(2025, 8, 31))  # 28 + 3 days
        self.assertEqual(state.last_attempt_date, date(2025, 8, 28))
        self.assertEqual(state.last_attempt_status, "Accepted")

    def test_first_attempt_failed_starts_in_l1(self):
        """A problem with only Failed submissions on the first day should start in box L1 (1-day interval).
        """
        problem = Problem(question_id="p2", title_slug="p2", difficulty="Medium")
        # Submitted on 2025-08-28
        sub = Submission(
            problem=problem,
            submitted_at=datetime(2025, 8, 28, 10, 0, 0),
            status="Wrong Answer",
            runtime="NA",
            memory="NA",
            file_path=""
        )
        problem.add_submission(sub)

        scheduler = LeitnerScheduler([problem], limit_days=30)
        state = scheduler.simulate_leitner(problem, date(2025, 8, 28))
        self.assertIsNotNone(state)
        self.assertEqual(state.box, "L1")
        self.assertEqual(state.next_due, date(2025, 8, 29))  # 28 + 1 day

    def test_subsequent_attempts_promotions_and_demotions(self):
        """Verify box progression and next_due calculations over multiple days.
        """
        problem = Problem(question_id="p3", title_slug="p3", difficulty="Hard")
        
        # Day 1: Passed -> Starts in L2, due on Day 4
        problem.add_submission(Submission(
            problem=problem,
            submitted_at=datetime(2025, 8, 1, 12, 0, 0),
            status="Accepted",
            runtime="10ms",
            memory="10MB",
            file_path=""
        ))
        
        # Day 4: Passed -> Solved on due date -> Promoted to L3, due on Day 11 (4 + 7)
        problem.add_submission(Submission(
            problem=problem,
            submitted_at=datetime(2025, 8, 4, 12, 0, 0),
            status="Accepted",
            runtime="10ms",
            memory="10MB",
            file_path=""
        ))
        
        # Day 11: Failed -> Demoted to L1, due on Day 12
        problem.add_submission(Submission(
            problem=problem,
            submitted_at=datetime(2025, 8, 11, 12, 0, 0),
            status="Time Limit Exceeded",
            runtime="NA",
            memory="NA",
            file_path=""
        ))

        scheduler = LeitnerScheduler([problem], limit_days=30)
        state = scheduler.simulate_leitner(problem, date(2025, 8, 28))
        self.assertIsNotNone(state)
        self.assertEqual(state.box, "L1")
        self.assertEqual(state.next_due, date(2025, 8, 12))

    def test_same_day_grouping_prevents_double_promotion(self):
        """Multiple submissions on the same calendar day should group into a single attempt day.
        If at least one is Accepted, it is a Passed day.
        """
        problem = Problem(question_id="p4", title_slug="p4")
        
        # Day 1: User fails twice, then accepts. All on 2025-08-01.
        # This counts as a single day attempt, and it Passed. Should start in L2 (due Day 4).
        problem.add_submission(Submission(problem, datetime(2025, 8, 1, 10, 0, 0), "Wrong Answer", "", "", ""))
        problem.add_submission(Submission(problem, datetime(2025, 8, 1, 10, 5, 0), "Wrong Answer", "", "", ""))
        problem.add_submission(Submission(problem, datetime(2025, 8, 1, 10, 10, 0), "Accepted", "", "", ""))
        
        scheduler = LeitnerScheduler([problem])
        state = scheduler.simulate_leitner(problem, date(2025, 8, 28))
        self.assertIsNotNone(state)
        self.assertEqual(state.box, "L2")
        self.assertEqual(state.next_due, date(2025, 8, 4))

    def test_limit_days_filters_old_problems(self):
        """Problems where the most recent attempt is older than limit_days should be excluded from due reminders.
        """
        p_active = Problem(question_id="active", title_slug="active")
        # Attempted 2 days ago relative to reference today
        p_active.add_submission(Submission(p_active, datetime(2025, 8, 26, 12, 0, 0), "Accepted", "", "", ""))

        p_old = Problem(question_id="old", title_slug="old")
        # Attempted 40 days ago relative to reference today
        p_old.add_submission(Submission(p_old, datetime(2025, 7, 19, 12, 0, 0), "Accepted", "", "", ""))

        problems = [p_active, p_old]
        
        # Reference date today = 2025-08-28. limit_days = 30
        today_ref = date(2025, 8, 28)
        scheduler = LeitnerScheduler(problems, limit_days=30)
        
        due_problems = scheduler.get_due_problems(today_ref)
        
        # p_active: next_due = Aug 29 (L2 because 26 + 3 days = Aug 29). Today is Aug 28. It is not due yet!
        # p_old: next_due is in the past, but it is excluded by the 30-day filter.
        # Therefore, due list should be empty.
        self.assertEqual(len(due_problems), 0)

        # Let's make p_active due today by adding a failure on Aug 27 (due next_due = 27 + 1 = 28)
        p_active.add_submission(Submission(p_active, datetime(2025, 8, 27, 12, 0, 0), "Wrong Answer", "", "", ""))
        due_problems = scheduler.get_due_problems(today_ref)
        
        self.assertEqual(len(due_problems), 1)
        self.assertEqual(due_problems[0]["problem"].question_id, "active")

    def test_get_upcoming_problems(self):
        """Verify that get_upcoming_problems correctly returns active problems that are not due yet.
        """
        p_future = Problem(question_id="future", title_slug="future")
        # Attempted 1 day ago. Started in L2 (due in 3 days -> Aug 30). Reference today is Aug 28.
        p_future.add_submission(Submission(p_future, datetime(2025, 8, 27, 12, 0, 0), "Accepted", "", "", ""))

        problems = [p_future]
        today_ref = date(2025, 8, 28)
        scheduler = LeitnerScheduler(problems, limit_days=30)

        due = scheduler.get_due_problems(today_ref)
        upcoming = scheduler.get_upcoming_problems(today_ref)

        self.assertEqual(len(due), 0)
        self.assertEqual(len(upcoming), 1)
        self.assertEqual(upcoming[0]["problem"].question_id, "future")
        self.assertEqual(upcoming[0]["state"].next_due, date(2025, 8, 30))

    def test_old_submissions_ignored_for_scheduling(self):
        """Submissions older than the active run window (limit_days) should not influence the Leitner box or next due date.
        """
        problem = Problem(question_id="p5", title_slug="p5")
        # An old submission (50 days ago relative to reference today of 2025-08-28 -> 2025-07-09)
        problem.add_submission(Submission(problem, datetime(2025, 7, 9, 12, 0, 0), "Accepted", "", "", ""))
        # A new submission (5 days ago -> 2025-08-23)
        problem.add_submission(Submission(problem, datetime(2025, 8, 23, 12, 0, 0), "Accepted", "", "", ""))

        today_ref = date(2025, 8, 28)
        scheduler = LeitnerScheduler([problem], limit_days=30)
        state = scheduler.simulate_leitner(problem, today_ref)
        
        self.assertIsNotNone(state)
        # The attempt on 2025-07-09 is older than 30 days, so it must be ignored.
        # The attempt on 2025-08-23 is the first active submission, starting in L2.
        self.assertEqual(state.box, "L2")
        self.assertEqual(state.next_due, date(2025, 8, 26)) # 23 + 3 days = 26
        # Today is Aug 28, so it is overdue by 2 days (due Aug 26)
        self.assertEqual((today_ref - state.next_due).days, 2)

if __name__ == "__main__":
    unittest.main()