tasks = []

def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['title']} [{status}]")

def mark_done():
    view_tasks()
    try:
        choice = int(input("Enter task number to mark done: "))
        tasks[choice - 1]["done"] = True
        print("Task marked as completed.")
    except:
        print("Invalid choice.")

def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        tasks.pop(choice - 1)
        print("Task deleted.")
    except:
        print("Invalid choice.")

while True:
    show_menu()
    option = input("Choose an option: ")

    if option == "1":
        add_task()
    elif option == "2":
        view_tasks()
    elif option == "3":
        mark_done()
    elif option == "4":
        delete_task()
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
