


# exercise 1
def is_even(n):
    even = n % 2 == 0
    return even

# exercise 2
def factorial(n):
    result = 1
    for i in range(n):
        result += (i+1) * result

    return result

# exercise 4
def is_palindrome(s):
    palin = s == s[::-1]
    return palin

# exercise 5
def sum_digits(n):
    sumi = 0
    run_loop = len(str(n))
    for i in range(run_loop):
        sumi += n % 10
        if i != run_loop:
            n = n // 10
    return sumi

def digital_root(n):
    result = n
    while len(str(result)) > 1:
        result = sum_digits(result)

    return result

# exercise 6
def count_digits(n):
    counter = 0
    while n:
        n = n//10
        counter += 1
    return counter

# exercise 7
def reverse_integer(n):
    result = 0
    l = len(str(n))
    for i in range(l):
        last_digit = n%10
        result += (10 ** (l-i-1)) * last_digit
        n = n // 10
    return result

# exercise 8
def integer_array(lst):
    l = len(lst)
    i = 0
    while l:
        if lst[i] == 0:
            zero = lst.pop(i)
            lst.append(zero)
        else:
            i += 1
        l -= 1
    return lst


# exercise 9
def list_numbers(lst):
    print(f"minimum: {min(lst)}")
    print(f"maximum: {max(lst)}")
    print(f"sum: {sum(lst)}")
    print(f"average: {round(sum(lst) / len(lst),2)}")
    return

# exercise 10
def reverse_list(lst):
    for i in range(len(lst)-1):
        last = lst.pop()
        lst.insert(i,last)
    return lst

# exercise 11
def repeating_values(lst):
    for num in lst:
        if lst.count(num) > 1:
            lst.remove(num)
    return lst

listi = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(repeating_values(listi))




