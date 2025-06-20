import datetime

class Task:
    def __init__(self, name: str, desc: str, deadline: datetime, complete: bool, priority: int):
        self.__name = name
        self.__desc = desc
        self.__deadline = deadline
        self.__complete = complete
        self.__priority = priority

    def __str__(self):
        return f"{self.__name} {self.__complete}"

    def MarkComplete(self):
        done = input("Is your task complete? (y for complete): ")
        if done.lower() == "y":
            self.__complete = True
        else:
            self.__complete = False

    def ViewDetailed(self):
        return (f"""Task: {self.__name}"
                Description: {self.__desc}"
                Deadline: {self.__deadline}"
                Completed?: {self.__complete}"
                Priority level: {self.__priority}""")
