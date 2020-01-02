class Book:
    def __init__(self, title="", authors=None):
        self.title = title
        self.authors = authors

    def __str__(self):
        return self.title + " by " + str(self.authors)
                
class Author:
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return self.firstName + " " + self.lastName

class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    @property
    def count(self):
        return len(self.__list)

    def __str__(self):
        author_str = ""
        for author in self.__list:
            author_str += str(author) + ", "
        author_str = author_str[:-2]  # strip last ", "
        return author_str

    # define the Authors object as the iterator
    def __iter__(self):
        self.__index = -1   # initialize index for each iteration
        return self

    # define the method that gets the next Author object
    def __next__(self):
        if self.__index == len(self.__list)-1:
            raise StopIteration         
        self.__index += 1
        author = self.__list[self.__index]
        return author
    
