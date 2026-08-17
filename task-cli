#!/usr/bin/env python3

import json
import sys
from datetime import datetime



DATA_FILE = "task.json"

def load_tasks():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(task_data):
    with open(DATA_FILE, "w") as f:
        json.dump(task_data, f)


def find_task(tasks, task_id):
    return next((item for item in tasks if item["id"] == task_id), None)


def int_task_id(raw_value):
    try:
        return int(raw_value)
    except ValueError:
        return None


def add_task(description):
    data = load_tasks()
    next_id = max((item["id"] for item in data), default=0) + 1

    new_task = {
        "id": next_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    data.append(new_task)
    save_tasks(data)
    print(f"Task successfully added (ID: {next_id}) :)")


def delete_task(task_id):
    data = load_tasks()
    task = find_task(data, task_id)
    if task is None:
        print("Task not found :(")
        return

    data = [item for item in data if item["id"] != task_id]
    save_tasks(data)
    print("Task successfully deleted :)")


def update_task(task_id, new_description):
    data = load_tasks()
    task = find_task(data, task_id)
    if task is None:
        print("Task not found :(")
        return

    task["description"] = new_description
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(data)
    print("Task successfully updated :)")


def change_status(task_id, new_status):
    data = load_tasks()
    task = find_task(data, task_id)
    if task is None:
        print("Task not found :(")
        return

    task["status"] = new_status
    task["updatedAt"] = datetime.now().isoformat()
    save_tasks(data)
    print("Task status successfully updated :)")


def list_tasks(status_filter=None):
    data = load_tasks()
    if status_filter:
        filtered = [item for item in data if item["status"] == status_filter]
    else:
        filtered = data

    if not filtered:
        print("List is empty!!")
        return

    for item in filtered:
        print(f'{item["id"]}. {item["description"]}  |  '
              f'Status: {item["status"]}\n'
              f'\nCreated: {item["createdAt"]} | Updated: {item["updatedAt"]}\n')



def main():
    print(
        '''    
        ╔══════════════════════════════════════════╗
        ║               Task Tracker               ║
        ╚══════════════════════════════════════════╝
        ''')

    if len(sys.argv) < 2:
        sys.exit("Error: Please, Pass at least ONE Argument!!")

    command = sys.argv[1]


    if command == "add":
        if len(sys.argv) < 3:
            sys.exit("Error: Please provide a task Description!!")
        add_task(sys.argv[2])


    elif command == "delete":
        if len(sys.argv) < 3:
            sys.exit("Error: Please provide a task ID!!")

        task_id = int_task_id(sys.argv[2])
        if task_id is None:
            sys.exit("Error: Task ID must be a number!! ")

        delete_task(task_id)


    elif command == "update":
        if len(sys.argv) < 4:
            sys.exit("Error: Please provide a task ID and description!!")
        task_id = int_task_id(sys.argv[2])
        if task_id is None:
            sys.exit("Error: Task ID must be a number!! ")

        update_task(task_id, sys.argv[3])


    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            sys.exit("Error: Please provide a task ID!!")
        task_id = int_task_id(sys.argv[2])
        if task_id is None:
            sys.exit("Error: Task ID must be a number!! ")

        change_status(task_id, "in-progress")


    elif command == "mark-done":
        if len(sys.argv) < 3:
            sys.exit("Error: Please provide a task ID!!")
        task_id = int_task_id(sys.argv[2])
        if task_id is None:
            sys.exit("Error: Task ID must be a number!! ")

        change_status(task_id, "done")


    elif command == "list":
        status_filter = sys.argv[2] if len(sys.argv) >= 3 else None
        if status_filter not in (None, "todo", "in-progress", "done"):
            sys.exit("Error: Invalid status. Use todo, in-progress, or done!!")
        list_tasks(status_filter)


    else:
        print("Error: Unknown Command!!")



if __name__ == "__main__":
    main()
