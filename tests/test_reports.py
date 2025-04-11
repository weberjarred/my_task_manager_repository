# Add the project root to the Python module search path (so that the imports
# from src/ work correctly) and uses the correct attribute names and
# import targets based on your provided source files.
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

import unittest
import os
from src.models import Task
from src.reports import generate_reports


class TestReports(unittest.TestCase):
    """
    TestReports is a test suite for verifying the functionality of the report
    generation process in the task manager project. It uses the unittest
    framework to ensure that the `generate_reports` function behaves as
    expected.

    Classes:
        TestReports: A unittest.TestCase subclass that contains test cases for
        validating the creation of report files.

    Methods:
        setUp(self):
            Prepares the test environment by initializing sample tasks
            and removing any existing report files to ensure a clean slate
            for each test.
        test_generate_reports_creates_files(self):
            Tests that the `generate_reports` function successfully creates the
            expected report files: "task_overview.txt" and "user_overview.txt".
        tearDown(self):
            Cleans up the test environment by removing any report files created
            during the test execution. This ensures a clean state for
            subsequent tests.
    """
    def setUp(self):
        """
        Set up the test environment for the report generation tests.

        This method initializes a list of sample tasks to be used in the tests
        and ensures that any existing report files ('task_overview.txt' and
        'user_overview.txt') are removed before each test to maintain a clean
        testing environment.
        """
        # Create sample tasks.
        self.tasks = [
            Task(
                "Alice", "Task1", "Desc1", "01 Jan 2025", "05 Jan 2025", "No"
            ),
            Task("Bob", "Task2", "Desc2", "02 Jan 2025", "06 Jan 2025", "Yes"),
        ]
        # Remove report files if they exist.
        if os.path.exists("task_overview.txt"):
            os.remove("task_overview.txt")
        if os.path.exists("user_overview.txt"):
            os.remove("user_overview.txt")

    def test_generate_reports_creates_files(self):
        """
        Test case for the `generate_reports` function.

        This test verifies that the `generate_reports` function successfully
        creates the expected report files: "task_overview.txt" and
        "user_overview.txt".

        Steps:
        1. Call the `generate_reports` function with the provided tasks.
        2. Assert that the file "task_overview.txt" exists in the current
           directory.
        3. Assert that the file "user_overview.txt" exists in the current
           directory.
        """
        generate_reports(self.tasks)
        self.assertTrue(os.path.exists("task_overview.txt"))
        self.assertTrue(os.path.exists("user_overview.txt"))

    def tearDown(self):
        """
        Clean up method that runs after each test case.

        This method checks for the existence of the files
        "task_overview.txt" and "user_overview.txt" in the current
        directory. If these files exist, they are removed to ensure
        a clean state for subsequent tests.
        """
        if os.path.exists("task_overview.txt"):
            os.remove("task_overview.txt")
        if os.path.exists("user_overview.txt"):
            os.remove("user_overview.txt")


if __name__ == "__main__":
    unittest.main()
