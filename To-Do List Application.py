# Build a TO-DO List Application using a simple Command Line Interface (CLI) that welcomes users and displays a menu with options to add, view, delete tasks, or quit the application.
# The tasks should be stored in a Python list.
# Alert the user if they provide invalid input.
# Alert the user if there are no tasks to view.
# Alert the user if they try to delete a task that doesn't exist.
# Alert the user if they select an option on the main menu that doesn't exist.
# Organize your code into functions to improve clarity and maintainability. 
# Use descriptive function names and add comments/docstrings where necessary.


task_list = []
def menu():
    '''Displays options available for selection'''
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Quit To-Do List")
    print("0. Menu")

def add_task():
    '''Add a task to To-Do List'''
    task = input("What task would you like to add? ")
    task_list.append(task)
    print(f"{task} has been added.")
def view_tasks():
    '''Sort and view tasks on the To-Do List'''
    if task_list == []:
        print("There are no tasks on the list.")
    else:
        task_list.sort() 
        print(f"To-Do List: {task_list}")

def delete_task():
    '''Deletes a task from the To-Do List'''
    if task_list == []:
        print("There are no tasks on the list.")
    else:
        task_list.sort()
        print(f" Items on list: {task_list}")  
        task = input("What task would you like to delete? ")
        task_list.remove(task)
        print(f"{task} has been deleted.")
name = input("Enter user name: ")
print(f"\nHello and Welcome {name} to your To-Do List!")
menu()

while True:
    option = input("\nPlease enter a numeric option from the choices above: ")
    try:
        if option == "1":
            add_task()
        elif option == "2":
            view_tasks()
        elif option == "3":
            delete_task()
        elif option == "4":
            print(f"Goodbye {name}!")
            break
        elif option == "0":
            menu()
        else:
            print("you have entered an invalid selection.")
    except ValueError:
        print("The task you have selected to delete is not on the list.")