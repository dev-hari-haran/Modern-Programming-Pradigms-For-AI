# Hariharan R
# Program: PR2 – Python Data Structures, Files, Modules & Error Handling
# Date: 24-01-26
# (e) Basic File Handling

with open("notes.txt", "w") as f:
    for _ in range(5):
        f.write(input("Enter line: ") + "\n")

with open("notes.txt", "r") as f:
    print("File Content:\n", f.read())

with open("notes.txt", "a") as f:
    f.write("End of notes\n")

