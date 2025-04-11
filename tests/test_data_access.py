# Add the project root to the Python module search path (so that the imports
# from src/ work correctly) and uses the correct attribute names and
# import targets based on your provided source files.
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


import unittest
from unittest.mock import patch
from src.data_access import load_tasks


class TestDataAccess(unittest.TestCase):
    """
    TestDataAccess is a test case class for testing the functionality of the
    `load_tasks` function in the `src.data_access` module.

    Methods:
        - test_load_tasks_file_not_found: Verifies that the `load_tasks`
          function correctly handles the scenario where the file it attempts
          to open does not exist, returning an empty list in such cases.
    """
    def test_load_tasks_file_not_found(self):
        """
        Test case for the `load_tasks` function when the file is not found.

        This test verifies that the `load_tasks` function correctly handles the
        scenario where the file it attempts to open does not exist. In such a
        case, the function is expected to return an empty list.

        Steps:
        1. Mock the `open` function in the `src.data_access` module to raise a
           `FileNotFoundError`.
        2. Call the `load_tasks` function.
        3. Assert that the returned value is an empty list.

        Expected Behaviour:
        - The `load_tasks` function should return an empty list when the file
          is not found.
        """
        # When the file is not found, load_tasks should return an empty list.
        with patch("src.data_access.open", side_effect=FileNotFoundError()):
            tasks = load_tasks()
            self.assertEqual(tasks, [])


if __name__ == "__main__":
    unittest.main()
