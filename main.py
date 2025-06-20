from task import Task
import datetime

def main():
    tasklist = []
    running = True

    while running == True:
        option = input("what would you like to do? ")

        if option == "add task":
            addTask(tasklist)
        elif option == "view tasks":
            viewTasks(tasklist)
        elif option == "delete task":
            deleteTask(tasklist)
        elif option == "mark complete":
            finishTask(tasklist)
        elif option == "view a task":
            getDetailedView(tasklist)
        else:
            print("Invalid option")

def getDetailedView(tasklst):
    taskpos = int(input("what task number would you like to view? ")) - 1
    print(tasklst[taskpos].ViewDetailed())


def finishTask(tasklst):
    taskpos = int(input("what task number would you like to finish? ")) - 1
    tasklst[taskpos].MarkComplete()
    print(f"task: {tasklst[taskpos]} has been completed")


def deleteTask(tasklst):
    if len(tasklst) == 0:
        print("There are no tasks to delete")
    else:
        taskpos = int(input("what task number would you like to delete? ")) - 1
        print(f"task: {tasklst.pop(taskpos)} has been removed")


def viewTasks(tasklst):
    if len(tasklst) == 0:
        print("you have no tasks")
    else:
        for i,tsk in enumerate(tasklst):
            print(f"{i+1}. {tsk}")


def addTask(tasklst):
    taskname = input("name of task: ")

    try:
        priority = int(input("priority (1,2,3): "))
    except:
        print("invalid format, default to priority 3")
        priority = 3

    desc = input("give your task a description: ")
    
    try:
        date = input("give the due date (dd-mm-yyyy): ")
        duedate = datetime.datetime.strptime(date, '%d-%m-%Y').date()
    except:
        duedate = None
        print("invalid date format, no date will be added")

    tasklst.append(Task(taskname, desc, duedate, False, priority))


if __name__ == '__main__':
    main()