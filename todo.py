def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # File does not exist yet
    return tasks

def save_tasks(tasks, filename):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter the new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added!")
    else:
        print("No task entered.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter the number of the task to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    FILENAME = 'tasks.txt'
    tasks = load_tasks(FILENAME)
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks, FILENAME)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks, FILENAME)
        elif choice == '4':
            save_tasks(tasks, FILENAME)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "_main_":
    main()
