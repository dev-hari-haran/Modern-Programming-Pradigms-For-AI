# Hariharan R
# Program: PR2 – Python Data Structures, Files, Modules & Error Handling
# Date: 24-01-26
# (b) Tuples and Immutability

students = []

for i in range(3):
    name = input("Enter name: ")
    roll = int(input("Enter roll: "))
    marks = float(input("Enter marks: "))
    students.append((name, roll, marks))

students = tuple(students)
print("Student Records:", students)

try:
    students[0][1] = 99
except TypeError as e:
    print("Tuple is immutable:", e)

name, roll, marks = students[0]
print("Unpacked Student:", name, roll, marks)

topper = max(students, key=lambda x: x[2])
print("Topper:", topper)
