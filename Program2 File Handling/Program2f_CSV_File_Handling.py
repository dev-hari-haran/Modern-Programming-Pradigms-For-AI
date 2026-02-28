# Hariharan R
# Program: PR2 – Python Data Structures, Files, Modules & Error Handling
# Date: 24-01-26
# (f) CSV File Handling

import csv

with open("employees.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "ID", "Salary"])
    writer.writeheader()

    for _ in range(3):
        writer.writerow({
            "Name": input("Name: "),
            "ID": input("ID: "),
            "Salary": float(input("Salary: "))
        })

employees = []
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["Salary"] = float(row["Salary"])
        employees.append(row)

print("Employee Data:", employees)
total_salary = sum(emp["Salary"] for emp in employees)
print("Total Salary:", total_salary)
