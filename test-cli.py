#!/usr/bin/env python3

import json
import sys
from datetime import datetime

print(
'''    
╔══════════════════════════════════════════╗
║               Task Tracker               ║
╚══════════════════════════════════════════╝
''')

if len(sys.argv) < 2:
    sys.exit("Error: Please, Pass at least ONE Argument!!")
else:
    command = sys.argv[1]

if command == "add":
    try:
        with open("task.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    next_id = max((item["id"] for item in data), default=0) + 1
    if len(sys.argv) < 3:
        sys.exit("Error: Please provide a task Description!!")
    else:
        description = sys.argv[2]
        k = {"id": next_id, "description": description, "status": "todo", "createdAt": datetime.now().isoformat(), "updatedAt": datetime.now().isoformat()}
        data.append(k)

    with open("task.json", "w") as file:
        json.dump(data, file)
    print("Task added successfully :)")


elif command == "update" :
    if len(sys.argv) < 4:
        sys.exit("Error: Please provide a task ID and description!!")
    try:
        with open("task.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    get_id = sys.argv[2]
    try:
        typecast = int(get_id)
    except ValueError:
        sys.exit("Please provide a valid task ID!!")
    new_description = sys.argv[3]
    find_id = next((item for item in data if item["id"] == typecast), None)
    if find_id is None:
        print("Task not found :(")
    else:
        find_id["description"] = new_description
        find_id["updatedAt"] = datetime.now().isoformat()
        with open("task.json", "w") as file:
            json.dump(data, file)
        print("Task Updated :)")

elif command == "delete" :
    if len(sys.argv) < 3:
        sys.exit("Error: Please provide a task ID!!")
    try:
        with open("task.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    try:
        typecast = int(sys.argv[2])
    except ValueError:
        sys.exit("Please provide task ID!!")

    find_id = next((item for item in data if item["id"] == typecast), None)
    if find_id is None:
        print("Task not found :(")
    else:
        data = [item for item in data if item["id"] != typecast]
        with open("task.json", "w") as file:
            json.dump(data, file)
        print("Task Deleted Successful :)\n")

elif command == "mark-in-progress" :
    if len(sys.argv) < 3:
        sys.exit("Error: Please provide a task ID!!")
    try:
        with open("task.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    get_id = sys.argv[2]
    try:
        typecast = int(get_id)
    except ValueError:
        sys.exit("Please provide task ID!!")
    find_id = next((item for item in data if item["id"] == typecast), None)
    if find_id is None:
        print("Task not found :(")
    else:
        find_id["status"] = "in-progress"
        find_id["updatedAt"] = datetime.now().isoformat()
        with open("task.json", "w") as file:
            json.dump(data, file)
        print("Task Status Updated :)")

elif command == "mark-done" :
    if len(sys.argv) < 3:
        sys.exit("Error: Please provide a task ID!!")
    try:
        with open("task.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    get_id = sys.argv[2]
    try:
        typecast = int(get_id)
    except ValueError:
        sys.exit("Please provide task ID!!")
    find_id = next((item for item in data if item["id"] == typecast), None)
    if find_id is None:
        print("Task not found :(")
    else:
        find_id["status"] = "done"
        find_id["updatedAt"] = datetime.now().isoformat()
        with open("task.json", "w") as file:
            json.dump(data, file)
        print("Task Status Updated :)")

elif command == "list":
    try:
        with open("task.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        sys.exit("List is Empty!!")
    if len(sys.argv) >=3:
        filtered = [item for item in data if item["status"] == sys.argv[2]]
    else:
        filtered = data
    for item in filtered:
        print(f'{item["id"]}. {item["description"]}  |  '
              f'Status: {item["status"]}\n'
              f'\nCreated: {item["createdAt"]} | Updated: {item["updatedAt"]}\n')

else:
    print("Error: Unknown Command!!")
