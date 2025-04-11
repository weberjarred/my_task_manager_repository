# Add the project root to the Python module search path (so that the imports
# from src/ work correctly) and uses the correct attribute names and
# import targets based on your provided source files.
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


import unittest
from unittest.mock import patch, mock_open
from src.services import capture_task


class TestServices(unittest.TestCase):
    """
    TestServices is a test suite for validating the functionality of the
    `capture_task` function.

    This test suite includes:
    - A single test case, `test_capture_task`, which verifies that the
      `capture_task` function correctly captures and appends a task to a
      task list based on user
        input.

    Test Case:
    - `test_capture_task`:
        - Simulates user input for capturing a task using the
          `@patch` decorator.
        - Mocks file operations using `mock_open`.
        - Asserts that the task list contains exactly one task after the
          function is called.
        - Validates that the attributes of the captured task (username,
          task title, task description, task due date, and task completion
          status) match the expected values.
    - `mock_file`: Mock object for file operations.
    - The task list contains exactly one task.
    - The attributes of the captured task match the following expected values:
        - `username`: "Bob"
        - `task_title`: "New Task"
        - `task_description`: "Task Description"
        - `task_due_date`: "10 Oct 2025"
        - `task_completion`: "No"
    """
    @patch(
        "builtins.input",
        side_effect=[
            "Bob",
            "New Task",
            "Task Description",
            "10 Oct 2025",
            "No",
        ],
    )
    @patch("src.services.open", new_callable=mock_open)
    def test_capture_task(self, mock_file, mock_input):
        """
        Test case for the `capture_task` function.

        This test verifies that the `capture_task` function correctly
        captures a task and appends it to the provided task list. It
        checks the following:
        - The task list contains exactly one task after the function
          is called.
        - The attributes of the captured task (username, task title,
          task description, task due date, and task completion status)
          match the expected values.

        Mocks:
        - `mock_file`: Mock object for file operations (if applicable).
        - `mock_input`: Mock object for simulating user input.

        Assertions:
        - The length of the task list is 1.
        - The attributes of the captured task match the expected values:
          - `username` is "Bob".
          - `task_title` is "New Task".
          - `task_description` is "Task Description".
          - `task_due_date` is "10 Oct 2025".
          - `task_completion` is "No".
        """
        task_list = []
        capture_task(task_list)
        self.assertEqual(len(task_list), 1)
        task = task_list[0]
        self.assertEqual(task.username, "Bob")
        self.assertEqual(task.task_title, "New Task")
        self.assertEqual(task.task_description, "Task Description")
        self.assertEqual(task.task_due_date, "10 Oct 2025")
        self.assertEqual(task.task_completion, "No")


if __name__ == "__main__":
    unittest.main()
