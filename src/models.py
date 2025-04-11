"""This module contains the Task class and defines any data models."""

"""Purpose: Define the data modules"""


class Task:
    """
    This class will contain the attributes of the task
    and the methods that will be used to manipulate the task.
    """
    # Constructor method
    def __init__(
        self,
        username,
        task_title,
        task_description,
        task_date_added,
        task_due_date,
        task_completion,
    ):
        self.username = username
        self.task_title = task_title
        self.task_description = task_description
        self.task_date_added = task_date_added
        self.task_due_date = task_due_date
        self.task_completion = task_completion

    # Method returns a string that represents the a Task object.
    def __str__(self):
        """
        Add a code to returns a string representation of a class.
        """
        return (
            f"Assigned to: {self.username}\n"
            f"Task Title: {self.task_title}\n"
            f"Description: {self.task_description}\n"
            f"Date of Assignment: {self.task_date_added}\n"
            f"Task Due Date: {self.task_due_date}\n"
            f"Task Completion: {self.task_completion}\n"
        )
