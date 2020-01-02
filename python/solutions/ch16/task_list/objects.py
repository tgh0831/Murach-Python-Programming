class Task:
    def __init__(self, description="", completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        completed_str = ""
        if self.completed == True:
            completed_str = " (DONE!)"            
        return self.description + completed_str
    
class TaskList:
    def __init__(self, name):
        self.name = name
        self.__tasks = []

    def addTask(self, task):
        self.__tasks.append(task)

    def getTask(self, number):
        index = number - 1
        task = self.__tasks[index]
        return task        

    def removeTask(self, task):
        self.__tasks.remove(task)

    def getCount(self):
        return len(self.__tasks)    

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index >= len(self.__tasks)-1:
            raise StopIteration()
        self.__index += 1
        task = self.__tasks[self.__index]
        return task

    def __str__(self):
        tasks_str = ""
        for task in self.__tasks:
            tasks_str += str(task) + " | "
        tasks_str = tasks_str[:-3]
        return tasks_str
