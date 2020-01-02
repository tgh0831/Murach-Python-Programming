import db
from objects import Task, TaskList

def display_task_list_names():
    names = db.get_task_list_names()
    print("TASK LISTS")
    i = 1
    for name in names:
        print(str(i) + ". " + name)
        i += 1
    print()

def list_tasks(tasks):
    if tasks.getCount() == 0:
        print("There are no tasks in this list.\n")
    else:
        i = 1
        for task in tasks:
            print(str(i) + ". " + str(task))
            i += 1
        print()

def add_task(tasks):
    description = input("Description: ")
    task = Task(description)
    tasks.addTask(task)
    print()

def delete_task(tasks):
    number = int(input("Number: "))
    task = tasks.getTask(number)
    tasks.removeTask(task)
    print()
        
def complete_task(tasks):
    number = int(input("Number: "))   
    task = tasks.getTask(number)
    task.completed = True
    print()
        
def display_menu():
    print("The Task List program")
    print()
    print("COMMAND MENU")
    print("list     - List all tasks")
    print("add      - Add a task")
    print("complete - Add a task")
    print("delete   - Delete a task")
    print("exit     - Exit program")
    print()

def main():
    display_menu()
    display_task_list_names()

    # select task list
    names = db.get_task_list_names()
    num = int(input("Enter number to select task list: "))
    name = names[num - 1]
    tasks = db.get_task_list(name)
    print(name + " task list was selected.\n")
    
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_tasks(tasks)     
        elif command.lower() == "add":
            add_task(tasks)
        elif command.lower() == "delete":
            delete_task(tasks)       
        elif command.lower() == "complete":
            complete_task(tasks)    
        elif command.lower() == "exit":
            db.write_task_list(name, tasks)
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()
