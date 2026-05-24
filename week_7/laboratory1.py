import os


# Exercise 1
with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("2024-01-15: There was a plenty day\n")
    f.write("2024-01-16: I learned about File Handling in python\n")
    f.write("2024-01-17: I completed the first exercise\n")
    print("The diary was created successfully")

with open("diary.txt", "r", encoding="utf-8") as f:
    print(f.read())



# Exercise 2
def add_entry(filename, date, content):
    with open(filename, "a", encoding="utf-8") as file1:
        file1.write(f"{date}: {content}\n")



def search_diary(file_name, keyword):
    try:
        with open(file_name, "r", encoding="utf-8") as fp:
            lines = fp.readlines()
            for row in lines:
                if row.find(keyword) != -1:
                    print(row.strip("\n"))
    except FileNotFoundError:
        print(f"{file_name} not found!")


def safe_read_diary(filename):
    return os.path.exists(filename)
