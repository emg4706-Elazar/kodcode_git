


# Exercise 1 -  Sum of a tuple
def sum_of_tuple(tupi):
    sumi = 0
    for n in tupi:
        sumi += n
    return sumi


# Exercise 2 - Maximum element
def max_num(tapi):
    maxi = tapi[0]
    for n in tapi:
        if maxi < n:
            maxi = n
    return maxi


# Exercise 3 -  Count occurrences
def count_of_value(tapi,value):
    counter = 0
    for val in tapi:
        if val == value:
            counter += 1
    return counter


# Exercise 4 - Reverse a tuple
def reverse_a_tuple(tupi):
    lst = []
    for i in range(len(tupi)-1,-1,-1):
        lst.append(tupi[i])
    return tuple(lst)


# Exercise 5 - Swap pairs
def swap_pairs(tupi):
    lst = []
    for i in range(len(tupi)):
        if i%2 == 0:
            lst.append(tupi[i])
        else:
            lst.insert(i-1,tupi[i])
    return tuple(lst)


# Exercise 6 - Min and max
def min_and_max_from_tuple(tupi):
    mini = tupi[0]
    maxi = tupi[0]
    for n in tupi:
        if n > maxi:
            maxi = n
        if n < mini:
            mini = n
    return mini, maxi


# Exercise 7 - Distance between points
def distance(tp1, tp2):
    x = [tp1[0], tp2[0]]
    y = [tp1[1], tp2[1]]
    dis = (((x[0] - x[1]) ** 2) + ((y[0] - y[1]) ** 2)) ** 0.5
    return dis


# Exercise 8 -  Merge and sort
def merge_and_sort(tp1, tp2):
    lst = tp1 + tp2
    return tuple(sorted(lst))


# Exercise 9 -  Frequency table
def frequency_table(tupi):
    unique_lst = []
    pairs_list = []
    for item in tupi:
        if item not in unique_lst:
            unique_lst.append(item)
    for current in unique_lst:
        counter = 0
        for item in tupi:
            if current == item:
                counter += 1
        pairs_list.append((current,counter))
    return tuple(pairs_list)


# Exercise 10 - Rotate a tuple
def rotate_a_tuple(tupi, k):
    lst = list(tupi)
    for i in range(k):
        last = lst.pop()
        lst.insert(0,last)
    return tuple(lst)
