"""
Purpose: This module handles reading from and writing to files.
File I/O: functions to load and save tasks.
"""

# from .models import Task  # Relative import of Task class from models

# The imports are now relative to the current package.
# i.e. relative imports.
# This tells Python to import Task from the models
# module within the same package.

from models import Task     # Absolute import of Task class from models


# ===================== Task / User Persistence ===================== #
def load_tasks():
    """
    Loads existing tasks from the 'task.txt' file into the in-memory task
    list and creates Task objects.

    Assumes each task is stored in 6 consecutive lines.

    The list called tasks will be used to store a list of objects of the Task
    class.

    Loads tasks from a file and returns them as a list of Task objects.
    This function reads the 'tasks.txt' file, where each task is stored in six
    consecutive lines with specific formatting. It parses the file content,
    creates Task objects, and appends them to a list. If the file is not found,
    an empty list is returned. Errors encountered while parsing individual
    tasks are logged, and the function continues processing the remaining
    tasks.

    Returns:
        list: A list of Task objects representing the tasks loaded
        from the file.

    Raises:
        FileNotFoundError: If the 'tasks.txt' file is not found.
        Exception: If there is an error parsing a specific task's data.
    """
    # ===================== Task list ===================== #
    tasks = []  # This list to store the tasks (Task objects) that are
    # created by the user.
    # ===================== Task list ===================== #

    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            # Remove blank lines and strip each line.
            lines = [line.strip() for line in lines if line.strip()]
            # Each task is 6 lines long.
            for i in range(0, len(lines), 6):
                try:
                    assigned_line = lines[i]
                    title_line = lines[i + 1]
                    desc_line = lines[i + 2]
                    date_assigned_line = lines[i + 3]
                    due_date_line = lines[i + 4]
                    completion_line = lines[i + 5]

                    username = assigned_line.split("Assigned to: ")[1].rstrip(
                        ","
                    )
                    task_title = title_line.split("Task Title: ")[1].rstrip(
                        ","
                    )
                    task_description = desc_line.split("Description: ")[
                        1
                    ].rstrip(",")
                    task_date_added = date_assigned_line.split(
                        "Date of Assignment: "
                    )[1].rstrip(",")
                    task_due_date = due_date_line.split("Task Due Date: ")[
                        1
                    ].rstrip(",")
                    task_completion = completion_line.split(
                        "Task Completion: "
                    )[1]
                    task = Task(
                        username,
                        task_title,
                        task_description,
                        task_date_added,
                        task_due_date,
                        task_completion,
                    )
                    tasks.append(task)
                except Exception as e:
                    print(
                        f"Error loading task from lines {i + 1} to {i + 6}: "
                        f"{e}"
                    )
                    continue
    except FileNotFoundError:
        print("tasks.txt file not found. Starting with an empty task list.")
    return tasks


def save_tasks(task_list):
    """
    This function writes the current (in-memory) task list to the 'tasks.txt'
    file.

    Saves the current list of tasks to a file.

    This function takes a list of task objects and writes their details
    to a file named 'tasks.txt'. Each task's information is written in
    a structured format with fields such as username, task title,
    description, date of assignment, due date, and completion status.

    Args:
        task_list (list): A list of task objects, where each object contains
                          attributes like username, task_title,
                          task_description,
                          task_date_added, task_due_date, and task_completion.

    Raises:
        Exception: If an error occurs during the file writing process,
        an exception is caught and an error message is printed to the console.
    """
    try:
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
    except Exception as e:
        print(f"Error saving tasks: {e}")
