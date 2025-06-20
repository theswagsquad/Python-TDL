class Task:
    def __init__(self, name: str, desc: str, deadline: datetime, complete: bool, priority: int):
        self.name = name
        self.desc = desc
        self.deadline = deadline
        self.complete = complete
        self.priority = priority

    def __str__(self):
        return f"{self.name} {self.complete}"
