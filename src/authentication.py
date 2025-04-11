import re
import getpass

"""Purpose: Manage user authentication, registration and authorization."""


# ===================== User Authentication Functions ===================== #
def is_valid_username(username):
    """
    Checks if there is at least one uppercase letter, one lowercase letter
    and the length of the username is between 5 and 20 characters
    returns True if the username is valid, otherwise returns False.
    """

    has_uppercase_letter = bool(re.search(r"[A-Z]", username))
    has_lowercase_letter = bool(re.search(r"[a-z]", username))
    is_between_5_and_20_characters = 5 <= len(username) <= 20
    return (
        has_uppercase_letter
        and has_lowercase_letter
        and is_between_5_and_20_characters
    )


def is_valid_password(password):
    """
    Checks if there os at least one uppercase letter, one lowercase letter,
    one digit and one special character returns True if the password is
    valid, otherwise returns False.
    """

    has_uppercase_letter = bool(re.search(r"[A-Z]", password))
    has_lowercase_letter = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special_char = bool(re.search(r"[^A-Za-z0-9]", password))
    return (
        has_uppercase_letter
        and has_lowercase_letter
        and has_digit
        and has_special_char
    )


def user_login(username, password):
    """
    This function will allow the user login and check if the username
    and password are correct by reading the user.txt file and checking
    if the username and password are in the file. If the username and
    password are correct, the function will return True.

    The function will prompt the user to enter their username and password
    If the username and password are incorrect, the function will return False.

    Thus::
    ===== Login Checking: =====

    Checks the provided username and password against entries in user.txt.
    Returns True if a matching record is found; otherwise returns False.
    The login function now properly compares the entered username/password
    with the stored values (instead of mistakenly calling the validation
    functions).

    The login section loops until a correct username/password combination is
    entered.
    """
    try:
        with open("user.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                stored_username, stored_password = line.split(", ")
                if stored_username == username and stored_password == password:
                    print("Username and password are accepted.\n")
                    print("You have successfully logged in.")
                    return True
        print("Invalid username or password. Please try again.\n")
        print(
            "Username must contain both uppercase and lowercase letters,"
            "and be between 5 and 20 characters long."
        )
        print(
            "Password must contain both uppercase and lowercase letters,"
            "a digit and a special character."
        )
        return False
    except FileNotFoundError:
        print("Error: User file not found. Please register first.")
        return False


def register_user():
    """
    This function will allow a user to register by adding their username and
    password to the user.txt file. The function will prompt the user to enter
    their username and password. The function will check if the username and
    password are valid, thus username and password will be validated, and the
    credentials will be written to the user.txt file.

    If the username and password are valid, the function will write the
    username and password to the user.txt file. If the username and password
    are invalid, the function will prompt the user to enter a valid username
    and password.

    ===== User Registration: =====
    Summary:: The file output format now simply writes the username and
    password separated by a comma (to match the login code). It also validates
    the new username and password using the provided validation functions,
    and ensures no duplicate username(s) exists in user.txt.

    Key points::  • Registration can only happen by the Administrator.
                  • Validation of username without any duplicate entries.
    """

    while True:
        new_username = input("Enter your username: ")
        username_duplicate_found = False

        # Check if the username already exists in the user.txt file.
        try:
            with open("user.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    stored_username, _ = line.split(", ")
                    if stored_username == new_username:
                        username_duplicate_found = True
                        break
        except FileNotFoundError:
            # If the file does not exist, there are no duplicate usernames.
            pass

        if username_duplicate_found:
            print(
                "Error: Username already exists. Please try again with a "
                "different username."
            )
            continue  # Skip the rest of the loop and start from the beginning.
            # Prompt the user to enter a new username.

        new_password = getpass.getpass("Enter your new password: ")
        confirm_new_password = getpass.getpass("Confirm your new password: ")

        if new_password != confirm_new_password:
            print("Error: Passwords do not match. Please try again.")
            return False
        else:
            if not is_valid_username(new_username):
                print(
                    "Error: Invalid username. Username must contain both "
                    "uppercase and lowercase"
                    "letters and be between 5 and 20 characters long."
                )
                return False
            if not is_valid_password(new_password):
                print(
                    "Error: Invalid password. Password must contain both "
                    "uppercase and lowercase letters,"
                    "a digit and a special character."
                )
                return False
            try:
                with open("user.txt", "a") as file:
                    file.write(f"{new_username}, {new_password}\n")
                    print("You have successfully registered a new user.")
                    return True
            except Exception as e:
                print(f"An error occurred while writing to file: {e}")
                return False
