import json
import os

FILE_PATH = "Z-CLI_based/To-do-list/to_Do.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:  # Overwrite the whole list
        json.dump(tasks, f, indent=4)

# Take user input initially
def user_input():
    print("Enter today's tasks (type 'END' to stop):")
    tasks = []
    while True:
        t = input("> ")
        if t.strip().upper() == "END":
            break
        tasks.append(t)
    
    save_tasks(tasks)
    return tasks

### Add new task
def add_task():
    tasks = load_tasks()
    new_task = input("Enter new task: ")
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added.")

### Delete a task by index
def delete_task():
    tasks = load_tasks()
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

#### Show all tasks
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

## Main menu operations
def to_do_list_operations():
    while True:
        print("\nMenu:\n1. Add New Task\n2. Delete Task\n3. Show All Tasks\n4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


def main():
    print("Welcome to your To-Do List!")
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        user_input()
    to_do_list_operations()

if __name__ == "__main__":
    main()
