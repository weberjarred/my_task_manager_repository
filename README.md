# Project Documentation

# Basic Task Manager Application

This project consolidated my learning by requiring the integration of multiple Python concepts, including File I/O, String and list manipulation, Conditionals and loops, Exception handling, Functions and Modularity, Optional Recursion, and Object-Oriented Programming Techniques, for a Basic Task Manager Application.

## 1. Project Structure

    task_manager_project/
    ├── src/
    │  ├── __init__.py
    │  ├── models.py
    │  ├── data_access.py
    │  ├── services.py
    │  ├── auth.py
    │  ├── reports.py
    │  ├── utilities.py
    │  └── main.py
    ├── tests/
    │  ├── __init__.py
    │  ├── test_models.py
    │  ├── test_data_access.py
    │  ├── test_services.py
    │  ├── test_auth.py
    │  └── test_reports.py
    ├── requirements.txt
    ├── README.md
    └── .flake8 (optional)
    └── .pyproject.toml

    OPTIONAL:
    For .flake8:
    [flake8]
    max-line-length = 79
    exclude = .git,__pycache__,tests,venv
    ignore = E203, E266, W503

    OPTIONAL:
    For .pyproject.toml:
    [tool.black]
    line-length = 79

## 2. Setup Instructions

1.  **Create a virtual environment.**

2.  **Check that flake8 extension works in particular project folder.**

3.  **Install flake8**

         Type: 'pip install flake8' into the vs code terminal.

4.  **Instal Black**

         Type: 'pip install black' into the vs code terminal.

         Run it on your codebase: Type: 'black example_file.py' for example_file
         formatting only, or 'black .' for formatting across the entire project folder.

5.  **Perform black and flake8 PEP 8 standards**

6.  **Run the application.**

    • From main.py module.

    • Move on to Unit Testing only after the application runs successfully.

    **NB: DISABLE RUN UNIT TESTS which are detailed in 7. i.e. comment out the relevant
    lines of code.**

7.  **Run Unit Tests.**

    Procedure for src folder modules (i. → ii.), and Procedure for tests folder (iii.):

          i. in data_access module, change 'from models import Task' → 'from .models import
          Task'

          ii. in services module, change 'from models import Task' → 'from .models import
          Task', and in services module, change 'from data_access import save_tasks' →
          'from .data_access import save_tasks'.

          iii. in all the tests files, insert the following code to the top of the module:

    #### Add the project root to the Python module search path (so that the imports

    #### from src/ work correctly) and uses the correct attribute names and

    #### import targets based on your provided source files.

          import sys
          import os
          sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
          iv. run each of the modules in the tests folder.

8.  **Generate requirements.exe file.**

         Run the following command from VS Code terminal:
         'pip freeze > requirements.txt'

## 3. Frequently used commands

This command recursively searches your project directory for any folders named pycache and deletes them.

    find . -type d -name "__pycache__" -exec rm -rf {} +

---

---
