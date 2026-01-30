# Hariharan R
# Program: PR2 – Python Data Structures, Files, Modules & Error Handling
# Date: 24-01-26
# (a) Advanced List Operations


nums = list(map(int, input("Enter integers (space-separated): ").split()))

evens = [x for x in nums if x % 2 == 0]
squares = [x**2 for x in nums]

nums_sorted = sorted(nums, reverse=True)

print("Even numbers:", evens)
print("Squares:", squares)
print("Sorted (desc):", nums_sorted)

print("Index with values:")
for i, v in enumerate(nums):
    print(i, "->", v)
