# to do list
class Task:
    def __init__(self, task_id, description, status="Incomplete"):
        self.task_id = task_id
        self.description = description
        self.status = status
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            print(f"{task.task_id}. [{task.status}] {task.description}")

    def update_task_status(self, task_id, new_status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = new_status
                break
def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Update Task Status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task_id = len(todo_list.tasks) + 1
            new_task = Task(task_id, description)
            todo_list.add_task(new_task)
            print("Task added successfully!")

        elif choice == "2":
            print("\n===== To-Do List =====")
            todo_list.display_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            new_status = input("Enter new status (Complete/Incomplete): ")
            todo_list.update_task_status(task_id, new_status)
            print("Task status updated successfully!")

        elif choice == "4":
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
