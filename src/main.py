import getpass
from data_access import load_tasks
from authentication import user_login, register_user
from services import (
    capture_task,
    view_all_tasks,
    view_my_tasks,
    view_completed_tasks,
    delete_task,
    modify_task,
)
from reports import generate_reports, display_statistics

"""Purpose: Serves as the entry point for the application."""


def main():
    # ============ Login Section Start ============ #
    # TODO: Implement the following functionality
    """
    Here you will write code that will allow a user to login.
    - Your code must read usernames and passwords from the user.txt file.
    - You can use a list or dictionary to store a list of usernames and
      passwords from the file.
    - Use a while loop to validate your user name and password.

    - Using getpass to HIDE the password while typing.
    """

    print("========== User Login ==========")
    print("Welcome to the Task Manager Application")
    print("Please enter login details to continue")

    logged_in = False
    while not logged_in:
        # Prompt the user to enter their username and password.
        user_username = input("Enter your username: ")
        user_password = getpass.getpass("Enter your password: ")

        # Call the function user_login to check if the username and
        # password are correct, and assign the result to logged_in
        logged_in = user_login(user_username, user_password)
    # ============ Login Section End ============ #

    # Load existing tasks from the 'task.txt' file into the in-memory task
    # list.
    task_list = load_tasks()

    # --------------------- Main program Loop --------------------- #
    """
    Program automatically loops back to the main menu after
    each task is completed. The program will additionally
    continue to run until the user selects the 'e' option to exit the program.
    """
    # Load and read the data from the file and create Task objects.

    # Loop continuously until the user enters the correct username and
    # password.
    while True:
        # Build dynamic menu based on the logged-in user.

        if user_username == "Administrator":
            menu = input(
                """\nSelect one of the following options:
                        • r - register a user
                        • a - add task
                        • va - view all tasks
                        • vm - view my tasks
                        • vc - view completed tasks
                        • del - delete a task
                        • mt - modify a task
                        • gr - generate reports
                        • ds - display statistics
                        • e - exit application

                        Enter selection: """
            ).lower()
        else:  # Present the menu to the user and make sure that the
            # user input is converted to lower case.
            menu = input(
                """\nSelect one of the following options:
                        • a - add task
                        • va - view all tasks
                        • vm - view my tasks
                        • mt - modify a task
                        • e - exit application

                        Enter selection: """
            ).lower()

        if menu == "r":
            # TODO: Implement the following functionality.
            """
            This code block will add a new user to the user.txt file
            - You can use the following steps:
                - Request input of a new username.
                - Request input of a new password.
                - Request input of password confirmation.
                - Check if the new password and confirmed password are the
                  same.
                - If they are the same, add them to the user.txt file,
                  otherwise present a relevant message.
            """

            # Only the Administrator can register a new user.
            # Call the function register_user to allow a user to register.
            if user_username == "Administrator":
                register_user()
            else:
                print("Error: Only the Administrator can register new users.")
                continue

        elif menu == "a":
            # TODO: Implement the following functionality.
            """
            This code block will allow a user to add a new task to
            task.txt file
            - You can use these steps:
                - Prompt a user for the following:
                    - the username of the person whom the task is assigned to,
                    - the title of the task,
                    - the description of the task, and
                    - the due date of the task.
                - Then, get the current date.
                - Add the data to the file task.txt
                - Remember to include 'No' to indicate that the task is not
                  complete.
            """
            # Call the function capture_task to allow a user to capture
            # data about a new task
            capture_task(task_list)

        elif menu == "va":
            # TODO: Implement the following functionality.
            """
            This code block will read the task from task.txt file and
            print to the console in the format of Output 2 presented in
            the PDF.

            You can do it in this way:
                - Read a line from the file.
                - Split that line where there is comma and space.
                - Then print the results in the format shown in the
                  Output 2 in the PDF.
                - It is much easier to read a file using a for loop.
            """
            # Call the function view_all_tasks to view all the tasks in the
            # task_list.
            view_all_tasks(task_list)

        elif menu == "vm":
            # TODO: Implement the following functionality.
            """
            This code block will read the task from task.txt file and
            print to the console in the format of Output 2 presented in
            the PDF.

            You can do it in this way:
                - Read a line from the file.
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same
                  as the username you have read from the file.
                - If they are the same you print the task in the format of
                  Output 2 shown in the PDF.
            """

            # Call the function view_my_tasks to view the tasks assigned to the
            # current user.
            view_my_tasks(user_username, task_list)

        elif menu == "vc":
            # Only Administrator can view completed tasks.
            if user_username == "Administrator":
                view_completed_tasks(task_list)
            else:
                print("Error: You are not authorized to view completed tasks.")

        elif menu == "del":
            # Only Administrator can delete tasks.
            if user_username == "Administrator":
                delete_task(task_list)
            else:
                print("Error: You are not authorized to delete tasks.")

        elif menu == "mt":
            # Call the function modify_task to allow the current user to
            # modify a task.
            modify_task(task_list, user_username)

        elif menu == "gr":
            # Call the function generate_reports to generate the reports.
            generate_reports(task_list)

        elif menu == "ds":
            # Call the function display_statistics to display the statistics.
            display_statistics(task_list)

        elif menu == "e":
            print("Goodbye!!!")
            exit()

        else:
            print("You have entered an invalid input. Please try again")


# --------------------- End of Main Program Loop --------------------- #

if __name__ == "__main__":
    main()
