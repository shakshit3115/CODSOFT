import json
import os
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Pending"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. Title: {task.title}, Description: {task.description}, Due Date: {task.due_date}, Status: {task.status}")

    def update_task_status(self, task_idx, new_status):
        if task_idx >= 0 and task_idx < len(self.tasks):
            self.tasks[task_idx].status = new_status

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [{"title": task.title, "description": task.description, "due_date": task.due_date, "status": task.status} for task in self.tasks]
            json.dump(tasks_data, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(task["title"], task["description"], task["due_date"]) for task in tasks_data]

def main():
    todo_list = ToDoList()

    # Load existing tasks from a file if it exists
    todo_list.load_from_file('tasks.json')

    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Update Task Status")
        print("4. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please enter date in the format YYYY-MM-DD.")
                continue

            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            todo_list.display_tasks()

        elif choice == '3':
            todo_list.display_tasks()
            task_idx = int(input("Enter the index of the task you want to update: ")) - 1
            new_status = input("Enter the new status for the task: ")
            todo_list.update_task_status(task_idx, new_status)
            print("Task status updated successfully.")

        elif choice == '4':
            todo_list.save_to_file('tasks.json')
            print("Tasks saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
