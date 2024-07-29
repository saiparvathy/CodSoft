def to_do_lt():
    tasks = []
    while True:
        print("\nTo-Do-List")
        print("Select Operation")
        print("1. Add New Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Exit")
        
        operation = input("Enter choice of operation (1/2/3/4/5): ")

        if operation == '1':
            task = input("Enter task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif operation == '2':
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' removed.")
            else:
                print("Task not found.")
        elif operation == '3':
            old_task = input("Enter task to update: ")
            if old_task in tasks:
                new_task = input("Enter new task: ")
                tasks[tasks.index(old_task)] = new_task
                print(f"Task '{old_task}' updated to '{new_task}'.")
            else:
                print("Task not found.")
        elif operation == '4':
            print("Current tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        elif operation == '5':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please enter a valid operation.")

to_do_lt()
