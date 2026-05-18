


# Exercise 1 -  Sum of value
def sum_values(dicti):
    sumi = 0
    for val in dicti.values():
        sumi += val
    return sumi


# Exercise 2 - Key with maximum value
def get_key_of_value(dicti):
    for k, v in dicti.items():
        if v == max(dicti.values()):
            return k
    return None


# Exercise 3 - Count characters
def count_characters(str1):
    dicti = {}
    for char in str1:
        dicti[char] = str1.count(char)
    return dicti


# Exercise 4 - Invert a dictionary
def invert_dict(dicti):
    new_dict = {}
    for k, v in dicti.items():
        new_dict[v] = k
    return new_dict


# Exercise 5 - Merge two dictionaries
def merge_dicts(d1, d2) -> dict:
    new_dict = {}
    for k, v in d1.items():
        new_dict[k] = v
    for k, v in d2.items():
        new_dict[k] = v
    return new_dict


# Exercise 6 - Filter by value
def filter_by_value(dicti, threshold):
    new_dict = {}
    for k, v in dicti.items():
        if v > threshold:
            new_dict[k] = v
    return new_dict


# Exercise 7 - Group by first letter
def group_by_first_letter(words):
    letters_lst = [ w[0] for w in words]
    new_dict = { l: [] for l in letters_lst}
    for w in words:
        new_dict[w[0]].append(w)
    return new_dict


# Exercise 8 - Word frequency
def word_frequency(str1):
    lst = str1.strip(" ").split(" ")
    dicti = {}
    for w in lst:
        dicti[w] = lst.count(w)
    return dicti


# Exercise 9 - Common keys
def common_keys(d1, d2):
    lst = []
    for key in d1:
        if d2.get(key) is not None:
            lst.append(key)
    return lst

# Exercise 10 - Most frequent value
def most_frequent_value(d):
    counts = {}
    for value in d.values():
        counts[value] = counts.get(value, 0) + 1
    return max(counts, key=counts.get)
