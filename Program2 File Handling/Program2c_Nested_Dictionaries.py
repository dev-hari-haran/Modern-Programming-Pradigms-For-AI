# Hariharan R
# Program: PR2 – Python Data Structures, Files, Modules & Error Handling
# Date: 24-01-26
# (c) Nested Dictionaries

class_data = {}

for _ in range(3):
    name = input("Student name: ")
    roll = int(input("Roll: "))
    math = float(input("Math marks: "))
    python = float(input("Python marks: "))

    class_data[name] = {
        "roll": roll,
        "subjects": {"Math": math, "Python": python}
    }

update_name = input("Enter student name to update Python marks: ")
if update_name in class_data:
    class_data[update_name]["subjects"]["Python"] = float(input("New Python marks: "))

for name, info in class_data.items():
    avg = sum(info["subjects"].values()) / 2
    print(f"{name} Average:", avg)

total_marks = {name: sum(info["subjects"].values()) for name, info in class_data.items()}
print("Total Marks:", total_marks)

