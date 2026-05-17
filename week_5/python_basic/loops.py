

# exercise 1
# for i in range(10):
#     if i == 7:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)

# exercise 2
# while True:
#     password = input("Enter your password!")
#     if password == "1234":
#         print("Wellcome!")
#         break
#     else:
#         print("Try again!")


# exercise 3
# names_lst = []
# active = True
# while active:
#     user_input = input("Enter a name product: ")
#     if user_input == "done":
#         active = False
#     else:
#         names_lst.append(user_input)
#
# if names_lst:
#     print(names_lst)
# else:
#     print("The list is empty")


# exercise 3 B
# for row in range(1,4):
#     for col in range(1,4):
#         if col == 2:
#             break
#         print(row,col)

# exercise 4
# total_vowels = 0
# str_user = input("Enter a string: ")
# for char in str_user:
#     if char.lower() in "aeiou":
#         total_vowels += 1
# print(f"total vowels:{total_vowels}")

# exercise 5
# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{j} * {i} = {i*j}")

# exercise 6
# str_user = input("Enter a string: ")
# temp = ""
# for i in range(0,len(str_user)):
#     temp += str_user[len(str_user)-i -1]
#
# print(temp)

# exercise 7
# even_digits_counter = 0
# num = 468
# while num:
#     if num % 2 == 0:
#         even_digits_counter += 1
#     num = num // 10
# print(even_digits_counter)

# exercise 8
str1 = "aabcffddk"
new_str = ""
last_char = ""
for char in str1:
    if not last_char:
        last_char = char
        continue
    if char == last_char:
        new_str = new_str + char
    last_char = char
print(new_str)













