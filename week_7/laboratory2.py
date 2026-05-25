

# Part A
def create_grades_file(filename):
    students = [
        ("Dan", [85, 90, 78]),
        ("MOMO", [92, 88, 95]),
        ("Yoni", [70, 65, 80]),
        ("Avi", [100, 95, 98]),
        ("Sara", [60, 72, 68])
    ]
    with open(filename, "w", encoding="utf-8") as f:
        for s in students:
            for item in s:
                if type(item) == list:
                    for grade in item:
                        f.write(str(f"{str(grade)},"))
                else:
                    f.write(str(f"{item},"))
            f.write("\n")
        print("The writing done successfully")


# Part B

def calculate_averages(filename):
    with open(filename, "r", encoding='utf-8') as f:
        lines = f.readlines()
    averages = {}
    for row in lines:
        lst_student = row.strip(",\n").split(",")
        key_name = lst_student.pop(0)
        sumi = 0
        for grade in lst_student:
            sumi += int(grade)
        average = round(sumi/len(lst_student),1)
        averages[key_name] = average

    return averages


# Part C
def save_results(averages, output_filename):
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("========Result Student========\n")
        result = {k: v for k, v in sorted(averages.items(),
                key=lambda item: item[1], reverse=True)}

        counter = 1
        for k, v in result.items():
            f.write(f"{counter}. {k}: {v}\n")
            counter += 1

        return


# Part C
def save_statistics(averages, output_filename):
    sorted_ave = {k: v for k, v in sorted(averages.items(),
                key=lambda item: item[1], reverse=True)}

    # calculate class average
    total_class = sum(list(sorted_ave.values()))
    num_students = len(list(sorted_ave.values()))
    class_average = round(total_class/num_students,1)

    # finding the highest and lowest student and his grade
    max_grade = list(sorted_ave.values())[0]
    min_grade = list(sorted_ave.values())[-1]
    highest = ""
    lowest = ""
    for k, v in averages.items():
        if v == max_grade:
            highest = f"{k} ({v})"
        if v == min_grade:
            lowest = f"{k} ({v})"

    # count how many students passed
    passing = 0
    for grade in sorted_ave.values():
        if grade <= 60:
            passing += 1


    # write into the file
    with open(output_filename, "a", encoding="utf-8") as f:
        f.write(f"\n\n========= Statistics =========\n")
        f.write(f"Class average: {class_average}\n")
        f.write(f"Highest: {highest}\n")
        f.write(f"Lowest: {lowest}\n")
        f.write(f"Passing (>=60) : {passing}/{num_students}")

    return