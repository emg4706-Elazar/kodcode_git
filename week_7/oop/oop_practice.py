


# Exercise 1
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof"


# Exercise 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


# Exercise 3
class Counter:
    """
    ========== Dockstring ===========
    class for counters.
    Each counter generate with default value 0.
    1. method increments(). Increase the value by 1
    2. method value(). return the current value.
    """

    def __init__(self, val=0):
        self.val = val


    def increment(self):
        self.val += 1

    def value(self):
        return self.val


# Exercise 4
class Point:
    """
    ======== dockstring =========
    point with x and y attributes
    methods:
        __str__ print the (x, y)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"



# Exercise 5
class BankAccount:
    """
    ======== Dockstring =========
    Attributes:
        _balance (int), with default value 0
    Methods:
        1. deposit(amount)
        2. withdraw(amount)
    """
    def __init__(self, balance=0):
        self._balance = balance


    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            return
        else:
            self._balance -= amount



# Exercise 6
class Temperature:
    """
    ======= Dockstring =======
    Attributes:
        1. Celsius(int)
    Method:
        1. to_fahrenheit(),
           returning the converted value.
    """
    def __init__(self, celsius):
        self._celsius = celsius

    def to_fahrenheit(self):
        converted = (self._celsius * 1.8) +32
        return converted


# Exercise 7
class Student:
    """
    ======== Dockstring ========
    Class attributes:
        1. school(str)
    Instance attributes:
        1. _name(str)
    """
    school = "Kodcode"
    def __init__(self, name1):
        self._name = name1


# Exercise 8
class Player:
    """
    ======== Dockstring ========
    Class attributes:
        1. counter_players(int)
    Instance attributes:
        1. _name(str)
    """
    counter_players = 0
    def __init__(self, name):
        self._name = name
        Player.counter_players += 1


# Exercise 9








