from task import task
import datetime

def main():
    tasklist = []
    run()


def run():
    return

def addTask(tasklst):
    taskname = input("name of task: ")
    priority = int(input("priority (1,2,3): "))
    desc = input("give your task a description: ")
    date = input("give the due date (dd-mm-yyyy): ")
    duedate = datetime.strptime(date, '%d-%m-%Y').date()
    tasklst.append(task(taskname, desc, duedate, False, priority))



if __name__ == '__main__':
    main()