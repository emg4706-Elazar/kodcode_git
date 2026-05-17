

# exercise1
# age = int(input("Enter your age: "))
# if age <= 0:
#     print("Invalid")
# elif 0 < age <= 12:
#     print("Child")
# elif 13 <= age <= 17:
#     print("Teen")
# else:
#     print("adult")

# exercise 2
# char = input("enter a char: ")
# if not "a" <= char <= "z":
#     print("Invalid")
#
# if char == "a" or "e" or "i" or "u" or "o":
#     print("Vowel")
#
# else:
#     print("Consonant")


# exercise 3
# age = int(input("Enter your age: "))
# if age < 16:
#     print("your entry rejected!")
# else:
#     has_a_card = input("Do you have a VIP card? ")
#     if  (age > 18 and has_a_card == "yes") or age == (19 or 20 or 21):
#         print("Entry allowed")
#
#     else:
#         print("your entry rejected!")


# exercise 4
# PASSWORD = "avi123"
# str1 = input("Enter a password: ")
# if PASSWORD == str1:
#     print("Access Granted")
# elif PASSWORD != str1 and len(str1) < 8:
#     print("Too short")
# else:
#     print("Wrong password")


# exercise 5
# print("Enter x and y coordinates!")
# x = float(input("x: "))
# y = float(input("y: "))
# if (10 <= x <= 50) and (20 <= y <= 80):
#     if (x == (10 or 50)) or (y == (20 or 80)):
#         print("On the edge")
#     else:
#         print("Inside the rectangle")
# else:
#     print("Outside the rectangle")

# exercise 6
# name = input("Enter your name: ")
# print("Wellcome",name or "Anonymous")

# exercise 8
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int( input("Enter third number: "))
# print((a > 0) + (b > 0) + (c > 0))

# exercise 10
score = int(input("Enter your score: "))
print("A" if 90 <score <=100 else "B" if 80 <= score <=90 else "C" if 70 <= score <=79 else "F")




