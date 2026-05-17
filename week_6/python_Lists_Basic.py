


# Exercise 1 - Sum of a list
def sum_of_list(lst):
    sumi = 0
    for n in lst:
        sumi += n
    return sumi


# Exercise 2 - Maximum element
def max_num(lst):
    maxi = lst[0]
    for n in lst:
        if n > maxi:
            maxi = n
    return maxi


# Exercise 3 - Count occurrences
def count_value(lst,val):
    counter = 0
    for n in lst:
        if n == val:
            counter += 1
    return counter


# Exercise 4 - Reverse a list
def reverse_lst(lst):
    new_list = []
    for i in range(len(lst)-1,-1,-1):
        new_list.append(lst[i])
    return new_list


# Exercise 5 - Remove duplicates
def rm_duplicate(lst):
    temp_list = []
    for n in lst:
        if n not in temp_list:
            temp_list.append(n)
    return temp_list


# Exercise 6 - Second largest
def sec_largest(lst):
    set_numbers = set(lst)
    if len(set_numbers) < 2:
        return None
    else:
        sec = sorted(list(set_numbers))
    return sec[-2]


# Exercise 7 - Merge two sorted lists
def merge_lists(l1,l2):
    l3 = l1 + l2
    return sorted(l3)


# Exercise 8 - Rotate a list
def rotate_a_list(lst,k):
    for i in range(k):
        last = lst.pop()
        lst.insert(0,last)
    return lst