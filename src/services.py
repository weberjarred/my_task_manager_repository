# from .models import Task  # Relative import of Task class from models

# The imports are now relative to the current package.
# i.e. relative imports.
# This tells Python to import Task from the models
# module within the same package.

from models import Task     # Absolute import of Task class from models

# from .data_access import save_tasks  # Relative import of save_tasks function
from datetime import date

from data_access import save_tasks   # Absolute import of save_tasks function

"""Business logic: adding, modifying, viewing, and deleting tasks."""

"""Purpose: Encapsulate the core task management functions."""


# ===================== Task Management Functions ===================== #
def capture_task(task_list):
    """
    This function allows a user to capture data about a new task,
    create a Task object with the provided data, append the object to
    the given task list, and update the tasks.txt file with the new
    task information.

    This function will allow a user to capture data
    about a (new) task and use this data to create a Task object
    and append this object inside the task list,
    and updates the tasks.txt file with the new data.

    Parameters:
        task_list (list): A list to which the newly created Task object
        will be appended.

    Functionality:
        - Prompts the user to input the username of the assignee, task title,
          task description, and task due date.
        - Automatically sets the task's assigned date to the current date.
        - Sets the task completion status to "No" by default.
        - Creates a Task object with the provided and generated data.
        - Appends the Task object to the provided task_list.
        - Writes the task details to the tasks.txt file in an append mode.

    Exceptions:
        - ValueError: Raised if invalid input is provided. This ensures
          that the input adheres to the expected format or constraints.
        - Exception: Catches any other errors that occur during the task
          creation or file writing process and displays an appropriate
          error message.

    Returns:
        None
    """
    try:
        # Get the user input for the new task.
        username = input(
            "Enter the username of the person the task is assigned to: "
        ).strip()
        task_title = input("Enter the title of the task: ").strip()
        task_description = input("Enter the description of the task: ").strip()

        # Set the assigned date to the current date.
        task_date_added = date.today().strftime("%d %b %Y")
        task_due_date = input("Enter the due date of the task: ").strip()

        # Default the task completion status to "No".
        task_completion = "No"

        # Create a new Task object with the captured user input data.
        new_task = Task(
            username,
            task_title,
            task_description,
            task_date_added,
            task_due_date,
            task_completion,
        )

        # Append the new Task object to the task_list.
        task_list.append(new_task)
        print("Task has been successfully added.")

        # Append the new task data to the task.txt file.
        with open("tasks.txt", "a") as file:
            file.write(
                f"\nAssigned to: {username},\n"
                f"Task Title: {task_title},\n"
                f"Description: {task_description},\n"
                f"Date of Assignment: {task_date_added},\n"
                f"Task Due Date: {task_due_date},\n"
                f"Task Completion: {task_completion}\n"
            )
        print(
            "Task file has been successfully updated "
            "(added) to the "
            "task.txt file."
        )
    except ValueError:
        print(
            "Error: Please enter a valid input corresponding to the above "
            "options"
        )
    except Exception as e:
        print(
            f"An error occurred while capturing and writing the new task data "
            f"to the file: {e}"
        )


def view_all_tasks(task_list):
    """
    Displays all tasks in a tabular format using the `tabulate` module or
    as plain text if the module is not installed.

    This function will iterate over the task_list and
    print the details of the tasks returned from the __str__
    function. Optional: I have organised the data in a tabular format
    by using Python’s tabulate module - chose fancy_grid tablefmt.

    Each task is displayed with a corresponding number for easy reference.

    Args:
        task_list (list): A list of task objects. Each task object is
            expected to have the following attributes:
            - username (str): The username of the person assigned to
              the task.
            - task_title (str): The title of the task.
            - task_description (str): A description of the task.
            - task_date_added (str): The date the task was assigned.
            - task_due_date (str): The due date of the task.
            - task_completion (str): The completion status of the task. This
              indicates whether the task is completed or not.

    Behaviour:
        - If the `task_list` is empty, a message is displayed indicating
          that there are no tasks to show.
        - If the `tabulate` module is installed, tasks are displayed
          in a tabular format with the "fancy_grid" style.
        - If the `tabulate` module is not installed, tasks are displayed as
          plain text with each task separated by a line.

    Raises:
        ImportError: If the `tabulate` module is not installed and the user
        attempts to view tasks in a tabular format.
    """
    if not task_list:
        print("There are no tasks to display in the list.")
        return

    try:
        from tabulate import tabulate

        # Create a list of lists containing the details of each task.
        header_line = [
            "Task No.",
            "Assigned to",
            "Task Title",
            "Description",
            "Date of Assignment",
            "Task Due Date",
            "Task Completion",
        ]
        task_data = [
            [
                i + 1,
                task.username,
                task.task_title,
                task.task_description,
                task.task_date_added,
                task.task_due_date,
                task.task_completion,
            ]
            for i, task in enumerate(task_list)
        ]

        # Print the table using the tabulate module.
        print(tabulate(task_data, headers=header_line, tablefmt="fancy_grid"))

    except ImportError:
        print(
            "Error: Please install the tabulate module to view the tasks in a "
            "tabular format."
        )
        for i, task in enumerate(task_list, 1):
            print(f"Task {i}:\n{task}\n")
            print("-" * 80)


def view_my_tasks(current_user, task_list):
    """
    Displays tasks assigned to the current user in an easy-to-read format.
    After displaying the tasks, the function prompts the user to select
    a task number.

    The nested recursive function get_valid_task_number() ensures
    that the input is valid.

    Parameters:
    - current_user (str): The username of the current user.
    - task_list (list): A list of Task objects.
    """

    # Filter the tasks assigned to the current user.
    user_tasks = [task for task in task_list if task.username == current_user]

    if not user_tasks:
        print("There are no tasks assigned to you.")
        return

    # Display the tasks assigned to the current user with a numbered list.
    print(f"\nTasks assigned to {current_user}:\n" + "-" * 80)
    for i, task in enumerate(user_tasks, 1):
        print(f"Task {i}:\n{task}\n")
        print(f" Title         : {task.task_title}")
        print(f" Description   : {task.task_description}")
        print(f" Date Assigned : {task.task_date_added}")
        print(f" Due Date      : {task.task_due_date}")
        print(f" Completed     : {task.task_completion}")
        print("-" * 80)


def view_completed_tasks(task_list):
    """
    Displays a list of tasks that have been marked as completed.
    This function filters the provided task list to identify tasks where the
    `task_completion` attribute is set to "Yes" (case-insensitive). If there
    are no completed tasks, a message is displayed indicating this.
    Otherwise, the completed tasks are printed in a formatted manner.

    Displays tasks that have been completed (i.e. task_completion
    equals "Yes"). Only the Administrator can access this option.

    Args:
        task_list (list): A list of task objects. Each task object is expected
                          to have a `task_completion` attribute.

    Returns:
        None: This function only prints the completed tasks or a message if
              there are no completed tasks.

    Note:
        This function is intended to be used by the Administrator only.
    """
    completed_tasks = [
        task for task in task_list if task.task_completion.lower() == "yes"
    ]

    if not completed_tasks:
        print("There are no completed tasks.")
        return

    print("\nCompleted Tasks" + " - " * 80)
    for i, task in enumerate(completed_tasks, 1):
        print(f"Task {i + 1}:\n{task}\n")
        print("-" * 80)


def delete_task(task_list):
    """
    Deletes a task from the task list based on user input.
    This function allows the user (Administrator) to delete a task by
    entering its corresponding number from the displayed list of tasks.
    The task list is updated in memory, and the changes are saved to
    the "tasks.txt" file.

    This function will allow the user to delete a task from the task list.
    Allows the Administrator to delete a task by entering its number.
    The task list is updated in memory and the task.txt file is rewritten.

    Args:
        task_list (list): A list of task objects, where each task contains
                          details such as username, task title, description,
                          date of assignment, due date, and completion status.

    Behaviour:
        - If the task list is empty, a message is displayed,
          and the function exits.
        - Displays all tasks with their index numbers for selection.
        - Prompts the user to input the task number to delete.
        - Validates the input to ensure it corresponds to a valid task number.
        - Removes the selected task from the task list and updates
          the "tasks.txt" file.
        - Handles invalid input gracefully by displaying appropriate error
          messages.

    Raises:
        ValueError: If the user enters a non-integer value for the task number.
    """
    if not task_list:
        print("No tasks available to delete.")
        return

    # List tasks with their index numbers.
    print("Current Tasks:")
    for i, task in enumerate(task_list, 1):
        print(f"{i}: {task.task_title} (Assigned to: {task.username})")
    try:
        task_num = int(input("Enter the task number to delete: "))
        if task_num < 1 or task_num > len(task_list):
            print("Invalid task number.")
            return
        deleted_task = task_list.pop(task_num - 1)
        print(f"Task '{deleted_task.task_title}' deleted successfully.")

        # Rewrite the task.txt file with the updated task list.
        with open("tasks.txt", "w") as file:
            for task in task_list:
                file.write(
                    f"Assigned to: {task.username},\n"
                    f"Task Title: {task.task_title},\n"
                    f"Description: {task.task_description},\n"
                    f"Date of Assignment: {task.task_date_added},\n"
                    f"Task Due Date: {task.task_due_date},\n"
                    f"Task Completion: {task.task_completion}\n"
                )
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def modify_task(task_list, current_user):
    """
    This function allows the CURRENT USER to select one of their tasks
    and either mark it as complete or edit it. Marking complete sets
    task_completion to "Yes". Editing allows the user to change the
    assigned username and / or due date, but only if the task is not
    completed. Tasks are displayed with their corresponding
    index numbers for easy selection.

    Tasks are displayed with their corresponding index numbers for easy
    selection.

    Parameters:
        task_list (list): A list of task objects, where each task contains
                          details such as username, task title, due date,
                          and completion status.
        current_user (str): The username of the currently logged-in user.

    Functionality:
        - Filters tasks assigned to the current user and displays them with
          index numbers.
        - Prompts the user to select a task by its displayed index number.
        - Allows the user to:
            - Mark the task as complete (if not already completed).
            - Edit the task's assigned username and/or due date (if the task
              is not completed).
        - Updates the task list and saves changes to the tasks file using
          `save_tasks()`. This ensures that the task list is updated
          both in memory and in the tasks file.
          in memory and in the tasks file.

    Returns:
        None: Prints messages to indicate the outcome of the operation, such as
              successful updates or errors (e.g., invalid task number
              or no tasks to modify).

    Notes:
        - If the user enters an invalid task number or cancels the operation,
          no changes are made.
        - Completed tasks cannot be edited.
    """

    # Filter tasks assigned to the current user with their original index.
    # Prompts the current user to choose a task (by number) to modify.
    user_tasks = [
        (i, task)
        for i, task in enumerate(task_list)
        if task.username == current_user
    ]
    if not user_tasks:
        print("You have no tasks to modify.")
        return

    print("\nYour Tasks:")
    for idx, task in user_tasks:
        print(
            f"{idx + 1}: {task.task_title} "
            f"(Due: {task.task_due_date}, "
            f"Completed: {task.task_completion})"
        )
    try:
        task_number = int(
            input(
                "Enter the task entry number you want to "
                "modify (If task is on line 1, enter 1 etc.): "
            )
        )
    except ValueError:
        print("Invalid task number.")
        return

    # Validate that the chosen task belongs to the current user.
    if task_number < 1 or task_number > len(user_tasks):
        print("Error: Invalid task number or task does not belong to you.")
        return

    selected_task = user_tasks[task_number - 1][1]
    # Prompt the user to choose an action: mark complete or edit task.
    # After modifications, save_tasks() is called to update the tasks.txt file.
    choice = input(
        "Enter 'c' to mark the task as complete, 'e' to edit the task, "
        "or any other key to cancel: "
    ).lower()
    if choice == "c":
        if selected_task.task_completion.lower() == "yes":
            print("Task is already marked as complete.")
        else:
            selected_task.task_completion = "Yes"
            save_tasks(task_list)
            print("Task marked as complete.")
    elif choice == "e":
        if selected_task.task_completion.lower() == "yes":
            print("Completed tasks cannot be edited.")
        else:
            new_assigned = input(
                f"Enter new assigned username "
                f"(or press Enter to keep '{selected_task.username}'): "
            ).strip()
            new_due_date = input(
                f"Enter new due date (or press Enter to keep "
                f"'{selected_task.task_due_date}'): "
            ).strip()
            if new_assigned:
                selected_task.username = new_assigned
            if new_due_date:
                selected_task.task_due_date = new_due_date
            save_tasks(task_list)
            print("Task updated successfully.")
    else:
        print("No changes made.")
