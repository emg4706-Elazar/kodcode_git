import math


# Exercise 1 - Counter with global
count = 0
def bump():
    global count
    count += 1

def value():
    return count


# Exercise 2 - Counter with closure
def make_counter():
    n = 0
    def inner_func():
        nonlocal n
        n += 1
        return n
    return inner_func


# Exercise 3 -  LEGB walk-through



# Exercise 8 -  Inspecting a module
def public_names(m):
    names_methods = dir(m)
    filterd = [n for n in names_methods if not n.startswith("_")]#filter(key= lambda n: not n.startswith("_"),names_methods)
    return filterd


# Exercise 9 - Avoid the mutable-default gotcha
















