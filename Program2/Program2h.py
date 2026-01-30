# Hariharan R
# Program: PR2 – Python Data Structures, Files, Modules & Error Handling
# Date: 24-01-26
# (h) Basic Error Handling
try:
    a = float(input("Enter number 1: "))
    b = float(input("Enter number 2: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid numeric input")

finally:
    print("Operation attempted")
