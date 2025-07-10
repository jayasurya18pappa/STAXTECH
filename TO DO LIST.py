todo_list = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Mark Task as Complete")
    print("5. Delete Task")
    print("6. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        for idx, task in enumerate(todo_list, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"{idx}. {task['title']} - {status}")

def add_task():
    title = input("Enter task title: ")
    todo_list.append({"title": title, "completed": False})
    print("Task added.")

def edit_task():
    view_tasks()
    index = int(input("Enter task number to edit: ")) - 1
    if 0 <= index < len(todo_list):
        new_title = input("Enter new task title: ")
        todo_list[index]["title"] = new_title
        print("Task updated.")
    else:
        print("Invalid task number.")

def complete_task():
    view_tasks()
    index = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= index < len(todo_list):
        todo_list[index]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(todo_list):
        removed = todo_list.pop(index)
        print(f"Deleted task: {removed['title']}")
    else:
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        edit_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
