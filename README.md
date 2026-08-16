# Task Tracker CLI

A lightweight Command Line Interface (CLI) application to track tasks and manage to-do lists, built with pure Python and JSON file persistence with zero third-party dependencies.

## Features

- **Add Tasks:** Create tasks with auto-incrementing IDs.
- **Update Tasks:** Modify task descriptions by ID.
- **Delete Tasks:** Remove tasks by ID.
- **Status Tracking:** Mark tasks as `todo`, `in-progress`, or `done`.
- **Filtered Listing:** List all tasks or filter by specific status.
- **Timestamps:** ISO format timestamps for `createdAt` and `updatedAt`.
- **Zero Dependencies:** Pure Python standard library (`sys`, `json`, `datetime`).

## Usage

```bash
# Add a task
python3 test-cli.py add "Buy groceries"

# List all tasks
python3 test-cli.py list

# List by status
python3 test-cli.py list done
python3 test-cli.py list todo
python3 test-cli.py list in-progress

# Update description
python3 test-cli.py update 1 "Buy groceries and cook dinner"

# Change status
python3 test-cli.py mark-in-progress 1
python3 test-cli.py mark-done 1

# Delete a task
python3 test-cli.py delete 1
