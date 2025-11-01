import os

tasks_file="F:\python programs\To-Do App\Tasks.txt" 

def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def save_tasks(tasks):
    f=open(tasks_file,"w", encoding='utf-8')
    for task in tasks:
        f.write(task + "\n")
    f.close()

def show_menu():
    print("TO DO LIST APP")
    print("1 : Show Tasks")
    print("2 : Add Tasks")
    print("3 : Remove Tasks")
    print("4 : Exit ")

tasks = load_tasks()

while True:
    show_menu()
    ch=int(input("Enter Your Choice : "))

    if ch==1:
        print("Your Tasks")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        if not tasks:
            print("No Tasks Yet.")
    elif ch==2:
        task=input("Enter task : ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added")
    elif ch==3 :
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        if not tasks:
            print("No tasks to remove.")
            continue
        try:
            num = int(input("Enter task number to remove : "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    elif ch==4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try Again.")