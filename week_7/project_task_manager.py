"""
A simple command-line To-Do List Manager.

This module allows the user to load tasks from a text file, save tasks,
add new tasks, mark existing tasks as done, and display all tasks.
Each task is stored in the file in the following format:
id|status|description
"""


def load_tasks(filename):
    """
    Load all tasks from a text file.

    The function reads each line from the given file, splits it into
    task ID, status, and description, and stores every task as a dictionary
    inside a list.

    Args:
        filename (str): The name or path of the file that contains the tasks.

    Returns:
        list[dict]: A list of task dictionaries. Each dictionary contains
        the keys "id", "status", and "description". If the file is not found,
        an empty list is returned.
    """
    lst_tasks = []
    try:
        with open(filename, "r", encoding='utf-8') as f:
            rows = f.readlines()
            for r in rows:
                task = {}
                idi, status, description = r.strip(" \n").split("|")
                task["id"] = idi
                task["status"] = status
                task["description"] = description
                lst_tasks.append(task)
                
    except FileNotFoundError:
        print(f"'{filename}' not found")

    return lst_tasks


def save_tasks(filename, tasks):
    """
    Save a list of tasks to the end of a text file.

    The function receives a list of task dictionaries and writes each task
    to the given file in the format: id|status|description.

    Args:
        filename (str): The name or path of the file where the tasks are saved.
        tasks (list[dict]): A list of task dictionaries. Each dictionary should
        contain the keys "id", "status", and "description".

    Returns:
        None
    """
    try:
        with open(filename, "a", encoding="utf-8") as f:
            for d in tasks:
                row = f"{d['id']}|{d['status']}|{d['description']}\n"
                f.write(row)
    except FileNotFoundError:
        print(f"'{filename}' not found")

    return


def add_task(filename, description):
    """
    Add a new task to the tasks file.

    The function counts the existing non-empty lines in the file in order
    to create a new task ID, and then appends the new task with a PENDING
    status to the end of the file.

    Args:
        filename (str): The name or path of the file where the task is added.
        description (str): The description of the new task.

    Returns:
        None
    """
    try:
        # get the last id
        with open(filename, "r", encoding="utf-8") as f:
            rows_count = 0
            for i in f:
                if i.isspace():
                    continue
                rows_count += 1
            new_id = rows_count + 1

        # add new task to the end of file
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{new_id}|PENDING|{description}\n")
    except FileNotFoundError:
        print(f"'{filename}' not found")

    return


def complete_task(filename, task_id):
    """
    Mark an existing task as done.

    The function loads all tasks from the file, searches for the task with
    the given ID, changes its status to DONE, and then rewrites the updated
    tasks back into the file. If the task ID does not exist, an error message
    is printed.

    Args:
        filename (str): The name or path of the file that contains the tasks.
        task_id (int | str): The ID of the task that should be marked as done.

    Returns:
        None
    """
    task_id = str(task_id)
    # get all the tasks from the file as list of dicts
    tasks = load_tasks(filename)

    # change the status
    for d in tasks:
        if d["id"] == str(task_id):
            d["status"] = "DONE"

    # check if 'task_id' is existed
    id_s = [d["id"] for d in tasks]
    if task_id not in id_s:
        print(f"ID:{task_id} does not exist")

    # rewrite into the file
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for d in tasks:
                f.write(f"{d['id']}|{d['status']}|{d['description']}\n")
    except FileNotFoundError:
        print(f"'{filename}' not found")

    return


def list_tasks(filename):
    """
    Display all tasks from the tasks file.

    The function loads all tasks and prints each task with its ID,
    description, and a visual status mark. Completed tasks are displayed
    with a check mark, and pending tasks are displayed with an empty box.

    Args:
        filename (str): The name or path of the file that contains the tasks.

    Returns:
        None
    """
    tasks = load_tasks(filename)
    for d in tasks:
        if d["status"] == "DONE":
            print(f"{d['id']} | {d['description']} | ✅")
        else:
            print(f"{d['id']} | {d['description']} | [ ]")

    return


def main():
    """
    Run the command-line To-Do List Manager.

    The function displays the main menu, receives the user's choice,
    and calls the relevant function according to the selected action:
    display tasks, add a task, mark a task as done, or exit the program.

    Args:
        None

    Returns:
        None
    """
    FILENAME = "tasks.txt"
    while True:
        print('\n=== To-Do List Manager ===')
        print('1. Display tasks ')
        print('2. Add task ')
        print('3. Mark as done ')
        print('4. Exit')
        choice = input('Choice: ')

        if choice == '1':
            list_tasks(FILENAME)
        elif choice == '2':
            desc = input(' Describe the task : ')
            add_task(FILENAME, desc)
            print(' The task added !')
        elif choice == '3':
            task_id = int(input(' Task number : '))
            complete_task(FILENAME, task_id)
        elif choice == '4':
            print('Good-bye!')
            break
        else:
            print(' Invalid Choice ')

    return


if __name__ == '__main__':
    main()
