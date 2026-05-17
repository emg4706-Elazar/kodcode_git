import random


# Exercise 1 - Safe int
def safe_int(s):
    try:
        return int(s)
    except:
        return None

# Exercise 2 - Safe divide
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"

# Exercise 3 -  Dictionary lookup with default
def get_value(d, key):
    try:
        return d[key]
    except:
        return "missing"

# Exercise 4 -  Parse list of ints
def parse_ints(values):
    l_of_ints = []
    for v in values:
        try:
            v = int(v)
            l_of_ints.append(v)
        except:
            continue
    return l_of_ints


# Exercise 5 - Validate age
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError
    else:
        return age

# Exercise 6 - Retry
def random_index():
    i = random.randint(0, 3)
    return i

def retry(func, n):
    lst = ["a","r","b","5"]
    for i in range(n):
        try:
            cast_to_int = int(lst[func()]) # func() returns random index
            return cast_to_int
        except:
            if i+1 == n:
                raise
            continue

# Exercise 7 -  Count errors
def count_errors(funcs):
    counter = 0
    for f in funcs:
        try:
            f()
        except:
            counter +=1
            continue
    return counter

# Exercise 8 -  Chained exceptions
def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            first_line = int(f.readline())
            return first_line
    except:
        raise RuntimeError("failed to loadconfig")






