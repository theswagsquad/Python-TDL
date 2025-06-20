from task import Task
import datetime

def main():
    tasklist = []
    running = True
    while running == True:
        option = input("what would you like to do?")
        if option == "add task":
            addTask(tasklist)
        elif option == "view tasks":
            viewTasks(tasklist)


def viewTasks(tasklst):
    if len(tasklst) == 0:
        print("you have no tasks")
    else:
        for i,tsk in enumerate(tasklst):
            print(f"{i}. {tsk}")


def addTask(tasklst):
    taskname = input("name of task: ")
    priority = int(input("priority (1,2,3): "))
    desc = input("give your task a description: ")
    date = input("give the due date (dd-mm-yyyy): ")
    duedate = datetime.datetime.strptime(date, '%d-%m-%Y').date()
    tasklst.append(Task(taskname, desc, duedate, False, priority))



if __name__ == '__main__':
    main()