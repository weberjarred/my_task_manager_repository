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
from src.authentication import is_valid_username, is_valid_password, user_login


class TestAuth(unittest.TestCase):
    """
    TestAuth is a test suite for validating the authentication functionality
    of the application.
    This class contains unit tests for the following:
    1. `is_valid_username` function:
        - Ensures that usernames meet the required criteria, such as
          containing at least one uppercase letter.
    2. `is_valid_password` function:
        - Validates that passwords meet the required criteria, including the
          presence of an uppercase letter, a digit, and a special character.
    3. `user_login` function:
        - Tests both successful and unsuccessful login attempts by mocking
          file operations to simulate stored user credentials.
    Test Methods:
    - `test_is_valid_username`: Verifies the correctness of the
      `is_valid_username` function.
    - `test_is_valid_password`: Ensures the `is_valid_password` function
      validates passwords accurately.
    - `test_user_login_success`: Tests successful login with valid credentials.
    - `test_user_login_failure`: Tests login failure with invalid credentials.
    Dependencies:
    - `unittest`: For creating and running the test cases.
    - `unittest.mock.patch`: For mocking file operations during login tests.
    """
    def test_is_valid_username(self):
        """
        Test case for the is_valid_username function.

        This test verifies that the is_valid_username function correctly
        identifies valid and invalid usernames based on the following criteria:
        - A valid username must contain at least one uppercase letter.

        Assertions:
        - Asserts that "AliceB" is a valid username.
        - Asserts that "alice" is an invalid username because it lacks
          an uppercase letter.
        """
        self.assertTrue(is_valid_username("AliceB"))
        self.assertFalse(is_valid_username("alice"))  # No uppercase letter

    def test_is_valid_password(self):
        """
        Test the `is_valid_password` function to ensure it correctly validates
        passwords.

        This test checks:
        - A valid password containing an uppercase letter, a digit,
          and a special character.
        - An invalid password missing the required criteria (uppercase
          letter, digit, and special character).
        """
        self.assertTrue(is_valid_password("Passw0rd!"))
        self.assertFalse(
            is_valid_password("password")
        )  # Missing uppercase, digit, special char

    @patch(
        "src.authentication.open",
        new_callable=mock_open,
        read_data="AliceB, Passw0rd!\n",
    )
    def test_user_login_success(self, mock_file):
        """
        Test case for successful user login.

        This test verifies that the `user_login` function returns True
        when provided with valid username and password credentials.

        Args:
            mock_file: A mock object for simulating file operations.

        Asserts:
            True if the login is successful with the given credentials.
        """
        self.assertTrue(user_login("AliceB", "Passw0rd!"))

    @patch(
        "src.authentication.open",
        new_callable=mock_open,
        read_data="AliceB, Passw0rd!\n",
    )
    def test_user_login_failure(self, mock_file):
        """
        Test case for user login failure.

        This test verifies that the `user_login` function returns `False`
        when provided with incorrect username and password credentials.

        Args:
            mock_file: A mocked file object used for testing purposes.

        Asserts:
            The `user_login` function should return `False` when the
            username is "AliceB" and the password is "WrongPassword".
        """
        self.assertFalse(user_login("AliceB", "WrongPassword"))


if __name__ == "__main__":
    unittest.main()
