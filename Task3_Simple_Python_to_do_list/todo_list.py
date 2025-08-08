import json
import os
from datetime import datetime

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({
            "task": task,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_tasks()
        print(f'Task added: "{task}"')

    def remove_task(self, task_name):
        for task in self.tasks:
            if task["task"].lower() == task_name.lower():
                self.tasks.remove(task)
                self.save_tasks()
                print(f'Task removed: "{task_name}"')
                return
        print("Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['task']} (Added: {task['created']})")

def main():
    todo = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice(1,2,3,4): ").strip()

        if choice == '1':
            task = input("Enter task: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == '2':
            task = input("Enter task to remove: ").strip()
            todo.remove_task(task)
        elif choice == '3':
            todo.view_tasks()
        elif choice == '4':
            print("Exiting...THANKU")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
