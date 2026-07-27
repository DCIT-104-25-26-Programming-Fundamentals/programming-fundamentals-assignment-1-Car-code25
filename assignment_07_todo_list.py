# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
tasks = []


def add_task():
    task = input("Enter task: ")
    tasks.append(task)

    print(f'Task added: "{task}"')


def view_tasks():
    if len(tasks) == 0:
        print("Your task list is empty.")
        return

    print("Your Tasks:")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task():
    if len(tasks) == 0:
        print("There are no tasks to delete.")
        return

    view_tasks()

    task_number = int(input("Enter task number to delete: "))

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    deleted_task = tasks.pop(task_number - 1)

    print(f'Task "{deleted_task}" has been removed.')


def main():
    while True:
        print()
        print("============================")
        print("       TO-DO LIST MENU")
        print("============================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")


main()
