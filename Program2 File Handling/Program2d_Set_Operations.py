# Hariharan R
# Program: PR2 – Python Data Structures, Files, Modules & Error Handling
# Date: 24-01-26
# (d) Set Operations


set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

print("Union:", set1.union(set2))
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

print("Is set1 subset of set2?", set1.issubset(set2))

set1.add(100)
print("Set1 after add:", set1)

if set2:
    set2.pop()
print("Set2 after remove:", set2)

fs = frozenset(set1)
print("Frozenset:", fs)

