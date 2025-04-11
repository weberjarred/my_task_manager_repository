import os
from datetime import date, datetime
from tabulate import tabulate

"""Purpose: Generate reports and statistics based on the tasks."""


# ===================== Reporting Functions ===================== #
def generate_reports(task_list):
    """
    Generates two reports:
    1. "task_overview.txt": Contains statistics about tasks.
    2. "user_overview.txt": Contains statistics about each user.

    Computes task overview (total tasks, completed, uncompleted, overdue,
    percentages) and writes these statistics to "task_overview.txt".
    It also reads user data from "user.txt" and computes per‑user
    statistics, writing these to "user_overview.txt".

    The function computes and writes the following statistics:
    1. Task Overview (written to "task_overview.txt"):
        - Total number of tasks.
        - Total number of completed tasks.
        - Total number of uncompleted tasks.
        - Total number of overdue tasks.
        - Percentage of tasks incomplete.
        - Percentage of tasks overdue.
    2. User Overview (written to "user_overview.txt"):
        - Total number of users.
        - Total number of tasks.
        - For each user:
          - Total tasks assigned.
          - Percentage of total tasks assigned.
          - Percentage of tasks completed.
          - Percentage of tasks incomplete.
          - Percentage of tasks overdue.

    Parameters:
         task_list (list): A list of task objects, where each task contains
                          attributes such as `task_completion`,
                          `task_due_date`, and `username`.

    Returns:
         None: The function writes the reports to files and prints a success
         message.
    """
    # --- Task Overview ---
    total_tasks = len(task_list)
    completed_tasks = sum(
        1 for task in task_list if task.task_completion.lower() == "yes"
    )
    uncompleted_tasks = total_tasks - completed_tasks
    today = date.today()
    overdue_tasks = 0
    for task in task_list:
        if task.task_completion.lower() != "yes":
            try:
                due_date = datetime.strptime(
                    task.task_due_date, "%d %b %Y"
                ).date()
                if due_date < today:
                    overdue_tasks += 1
            except Exception:
                continue
    pct_incomplete = (
        (uncompleted_tasks / total_tasks * 100) if total_tasks else 0
    )
    pct_overdue = (overdue_tasks / total_tasks * 100) if total_tasks else 0

    # Write task overview report to task_overview.txt.
    try:
        with open("task_overview.txt", "w") as file:
            file.write(f"Total number of tasks: {total_tasks}\n")
            file.write(f"Total number of completed tasks: {completed_tasks}\n")
            file.write(
                f"Total number of uncompleted tasks: {uncompleted_tasks}\n"
            )
            file.write(f"Total number of overdue tasks: {overdue_tasks}\n")
            file.write(
                f"Percentage of tasks incomplete: {pct_incomplete:.2f}%\n"
            )
            file.write(f"Percentage of tasks overdue: {pct_overdue:.2f}%\n")
    except Exception as e:
        print(f"Error writing task_overview.txt: {e}")

    # --- User Overview ---
    users = []
    try:
        with open("user.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    u, _ = line.split(", ")
                    if u not in users:
                        users.append(u)
    except FileNotFoundError:
        print("User file not found.")

    total_users = len(users)
    user_report_lines = []
    user_report_lines.append(f"Total number of users: {total_users}")
    user_report_lines.append(f"Total number of tasks: {total_tasks}\n")

    for u in users:
        tasks_for_u = [task for task in task_list if task.username == u]
        num_tasks_for_u = len(tasks_for_u)
        pct_total = (num_tasks_for_u / total_tasks * 100) if total_tasks else 0
        completed_for_u = sum(
            1 for task in tasks_for_u if task.task_completion.lower() == "yes"
        )
        pct_completed = (
            (completed_for_u / num_tasks_for_u * 100) if num_tasks_for_u else 0
        )
        pct_incomplete = (
            ((num_tasks_for_u - completed_for_u) / num_tasks_for_u * 100)
            if num_tasks_for_u
            else 0
        )
        overdue_for_u = 0
        for task in tasks_for_u:
            if task.task_completion.lower() != "yes":
                try:
                    due_date = datetime.strptime(
                        task.task_due_date, "%d %b %Y"
                    ).date()
                    if due_date < today:
                        overdue_for_u += 1
                except Exception:
                    continue
        pct_overdue = (
            (overdue_for_u / num_tasks_for_u * 100) if num_tasks_for_u else 0
        )
        user_report_lines.append(f"User: {u}")
        user_report_lines.append(f"  Total tasks assigned: {num_tasks_for_u}")
        user_report_lines.append(
            f"  % of total tasks assigned: {pct_total:.2f}%"
        )
        user_report_lines.append(
            f"  % of tasks completed: {pct_completed:.2f}%"
        )
        user_report_lines.append(
            f"  % of tasks incomplete: {pct_incomplete:.2f}%"
        )
        user_report_lines.append(f"  % of tasks overdue: {pct_overdue:.2f}%\n")

    try:
        with open("user_overview.txt", "w") as file:
            file.write("\n".join(user_report_lines))
    except Exception as e:
        print(f"Error writing user_overview.txt: {e}")

    print("Reports generated successfully.")


def display_statistics(task_list):
    """
    Displays task and user statistics in a tabular format.
    This function ensures that the necessary report files exist
    by generating them if they are missing. It then computes and displays
    two tables: one for task overview statistics and another for user
    overview statistics. The tables are formatted using the `tabulate`
    library for better readability.

    Generates the reports first if they do not already exist.

    Ensures that the report files exist (by calling generate_reports
    if needed) and then recomputes the statistics, displaying
    two user‑friendly tables (one for task overview and one
    for user overview) using tabulate.

    Task Overview Statistics:
    - Total number of tasks.
    - Number of completed tasks.
    - Number of uncompleted tasks.
    - Number of overdue tasks.
    - Percentage of incomplete tasks.
    - Percentage of overdue tasks.

    User Overview Statistics:
    - Username.
    - Number of tasks assigned to each user.
    - Percentage of total tasks assigned to each user.
    - Percentage of tasks completed by each user.
    - Percentage of tasks incomplete for each user.
    - Percentage of tasks overdue for each user.

    Args:
        task_list (list): A list of task objects, where each task contains
                          details such as username, task completion status,
                          and due date.

    Raises:
        FileNotFoundError: If the user file (`user.txt`) is not found,
            a message is printed, and the user overview statistics
            are skipped.
    """
    # Ensure reports exist by generating them.
    if not os.path.exists("task_overview.txt") or not os.path.exists(
        "user_overview.txt"
    ):
        generate_reports(task_list)

    # --- Task Overview Statistics ---
    total_tasks = len(task_list)
    completed_tasks = sum(
        1 for task in task_list if task.task_completion.lower() == "yes"
    )
    uncompleted_tasks = total_tasks - completed_tasks
    today = date.today()
    overdue_tasks = 0
    for task in task_list:
        if task.task_completion.lower() != "yes":
            try:
                due_date = datetime.strptime(
                    task.task_due_date, "%d %b %Y"
                ).date()
                if due_date < today:
                    overdue_tasks += 1
            except Exception:
                continue
    pct_incomplete = (
        (uncompleted_tasks / total_tasks * 100) if total_tasks else 0
    )
    pct_overdue = (overdue_tasks / total_tasks * 100) if total_tasks else 0

    task_overview_data = [
        ["Total Tasks", total_tasks],
        ["Completed Tasks", completed_tasks],
        ["Uncompleted Tasks", uncompleted_tasks],
        ["Overdue Tasks", overdue_tasks],
        ["% Incomplete", f"{pct_incomplete:.2f}%"],
        ["% Overdue", f"{pct_overdue:.2f}%"],
    ]

    # --- User Overview Statistics ---
    users = []
    try:
        with open("user.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    u, _ = line.split(", ")
                    if u not in users:
                        users.append(u)
    except FileNotFoundError:
        print("User file not found.")
        users = []

    user_overview_data = []
    for u in users:
        tasks_for_u = [task for task in task_list if task.username == u]
        num_tasks_for_u = len(tasks_for_u)
        pct_total = (num_tasks_for_u / total_tasks * 100) if total_tasks else 0
        completed_for_u = sum(
            1 for task in tasks_for_u if task.task_completion.lower() == "yes"
        )
        pct_completed = (
            (completed_for_u / num_tasks_for_u * 100) if num_tasks_for_u else 0
        )
        pct_incomplete_u = (
            ((num_tasks_for_u - completed_for_u) / num_tasks_for_u * 100)
            if num_tasks_for_u
            else 0
        )
        overdue_for_u = 0
        for task in tasks_for_u:
            if task.task_completion.lower() != "yes":
                try:
                    due_date = datetime.strptime(
                        task.task_due_date, "%d %b %Y"
                    ).date()
                    if due_date < today:
                        overdue_for_u += 1
                except Exception:
                    continue
        pct_overdue_u = (
            (overdue_for_u / num_tasks_for_u * 100) if num_tasks_for_u else 0
        )
        user_overview_data.append(
            [
                u,
                num_tasks_for_u,
                f"{pct_total:.2f}%",
                f"{pct_completed:.2f}%",
                f"{pct_incomplete_u:.2f}%",
                f"{pct_overdue_u:.2f}%",
            ]
        )

    # Display the tables.
    print("\nTASK OVERVIEW REPORT:")
    print(
        tabulate(
            task_overview_data,
            headers=["Metric", "Value"],
            tablefmt="fancy_grid",
        )
    )
    print("\nUSER OVERVIEW REPORT:")
    headers = [
        "Username",
        "Tasks Assigned",
        "% of Total Tasks",
        "% Completed",
        "% Incomplete",
        "% Overdue",
    ]
    print(tabulate(user_overview_data, headers=headers, tablefmt="fancy_grid"))
