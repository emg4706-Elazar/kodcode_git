


# Exercise 1 - Remove duplicates
def remove_duplicates(lst):
    seti = set(lst)
    return list(seti)


# Exercise 2 - Count unique elements
def count_unique_elements(lst):
    seti = set(lst)
    counter = 0
    for n in seti:
        counter += 1
    return counter


# Exercise 3 - Common elements
def common_elements(lst1, lst2):
    seti = set(lst1) & set(lst2)
    cast_to_list = list(seti)
    return sorted(cast_to_list)


# Exercise 4 -  Elements in only one
def  elements_in_only_one(lst1, lst2):
    seti = set(lst1) ^ set(lst2)
    cast_to_list = list(seti)
    return sorted(cast_to_list)


# Exercise 5 - Is subset
def is_subset(lst1, lst2):
    a = set(lst1)
    b = set(lst2)
    return a <= b


# Exercise 6 - Unique characters
def unique_characters(str1):
    cast_to_list = list(str1)
    cast_to_set = set(cast_to_list)
    return len(cast_to_set) == len(cast_to_list)


# Exercise - 7 - First repeated element
def first_repeated_element(lst):
    seti = set({})
    for val in lst:
        if val not in seti:
            seti.add(val)
        else:
            return val
    return None


# Exercise 8 - Distinct words
def distinct_words(str1):
    seti = set({})
    cast_to_list = str1.strip(" ").split(" ")
    for w in cast_to_list:
        seti.add(w.lower())
    return len(seti)


# Exercise 9 - Pair sum exists
def pair_sum_exists(lst, target) -> bool:
    cast_to_set = set(lst)
    seen = set()
    for n in cast_to_set:
        if (target-n) in seen:
            return True
        else:
            seen.add(n)
    return False


# Exercise 10 - Symmetric difference without operators
def symmetric_diffs(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    diff1 = set1.difference(set2)
    diff2 = set2.difference(set1)
    return sorted(list(diff1.union(diff2)))
