import random

class Die:
    def __init__(self):
        self.__value = self.roll()

    @property
    def value(self):
        return self.__value
                
    @value.setter
    def value(self, value):
        if value < 1:
            raise ValueError("Die can't be less than 1.")
        elif value > 6:
            raise ValueError("Die can't be more than 6.")
        else:
            self.__value = value
                
    @property
    def image(self):
        if self.__value == 6:
            image = " _____ \n" + \
                    "|o   o|\n" + \
                    "|o   o|\n" + \
                    "|o___o|"
            return image
        elif self.__value == 5:
            return " _____ \n" + \
                   "|o   o|\n" + \
                   "|  o  |\n" + \
                   "|o___o|"
        elif self.__value == 4:
            return " _____ \n" + \
                   "|o   o|\n" + \
                   "|     |\n" + \
                   "|o___o|"
        elif self.__value == 3:
            return " _____ \n" + \
                   "|o    |\n" + \
                   "|  o  |\n" + \
                   "|____o|"
        elif self.__value == 2:
            return " _____ \n" + \
                   "|o    |\n" + \
                   "|     |\n" + \
                   "|____o|"
        elif self.__value == 1:
            return " _____ \n" + \
                   "|     |\n" + \
                   "|  o  |\n" + \
                   "|_____|"
                
    def roll(self):
        self.__value = random.randrange(1, 7)
        return self.__value
                
class Dice:
    def __init__(self):
        self.__list = []

    def addDie(self, die):
        self.__list.append(die)

    @property
    def list(self):
        dice_tuple = tuple(self.__list)
        return dice_tuple
                
    def rollAll(self):
        for die in self.__list:
            die.roll()

    def getTotal(self):
        total = 0
        for die in self.__list:
            total += die.value
        return total
