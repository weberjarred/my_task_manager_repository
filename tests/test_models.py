# Add the project root to the Python module search path (so that the imports
# from src/ work correctly) and uses the correct attribute names and
# import targets based on your provided source files.
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

import unittest
from src.models import Task


class TestTaskModel(unittest.TestCase):
    """
    TestTaskModel is a test case class for testing the Task model.
    This class contains unit tests to verify the behavior and functionality
    of the Task model, specifically focusing on its string representation.

    Methods:
        test_str_representation:
            Tests the __str__ method of the Task class to ensure it returns
            the expected string format, including details such as the assignee,
            task title, description, assignment date, due date, and completion
            status.
    """
    def test_str_representation(self):
        """
        Test the string representation of the Task model.

        This test verifies that the __str__ method of the Task class
        returns the expected string format, which includes details
        such as the assignee, task title, description, assignment date,
        due date, and completion status.
        """
        task = Task(
            "Alice",
            "Test Task",
            "Description",
            "01 Jan 2025",
            "05 Jan 2025",
            "No",
        )
        expected = (
            "Assigned to: Alice\n"
            "Task Title: Test Task\n"
            "Description: Description\n"
            "Date of Assignment: 01 Jan 2025\n"
            "Task Due Date: 05 Jan 2025\n"
            "Task Completion: No\n"
        )
        self.assertEqual(str(task), expected)


if __name__ == "__main__":
    unittest.main()
