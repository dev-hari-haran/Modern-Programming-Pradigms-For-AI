#Start
#Hariharan R
#23-01-2026
#Program for Functions with Variable Arguments (*args and **kwargs) with Loop

def student_info(name, roll, *marks, **details):
    """
    Function to accept variable marks and variable keyword details.
    """
    print("\n========== STUDENT PROFILE ==========")
    print("Name:", name)
    print("Roll Number:", roll)
    
    # Handling *marks (Variable Positional Arguments)
    print("\n--- Marks Statement ---")
    total_marks = 0
    for m in marks:
        print("Subject Mark:", m)
        total_marks = total_marks + m
    print("Total Marks Scored:", total_marks)
    
    # Handling **details (Variable Keyword Arguments)
    print("\n--- Additional Information ---")
    for key, value in details.items():
        print(key, ":", value)
    print("=====================================")

# Main Program Execution
print("Select Mode:")
print("1. Automated Mode (Pre-defined values)")
print("2. Manual Mode (User Input - Loop)")
mode = input("Enter your choice (1 or 2): ")

if mode == '1':
    # Automated Mode: 4 marks and 3 keyword details
    print("\nRunning in Automated Mode...")
    student_info("Hariharan", "CS101", 90, 85, 92, 88, 
                 Branch="Python", 
                 Semester="4th", 
                 City="Chennai")

elif mode == '2':
    # Manual Mode with Loop
    print("\nRunning in Manual Mode...")
    
    while True: # Start of the continuous loop
        print("\n--- New Entry ---")
        u_name = input("Enter Name: ")
        u_roll = input("Enter Roll Number: ")
        
        # Input for Marks
        marks_input = input("Enter 4 marks separated by space (e.g., 90 80 70 60): ")
        # Map splits the string and converts items to int
        marks_list = list(map(int, marks_input.split()))
        
        # Input for Details
        u_branch = input("Enter Branch: ")
        u_sem = input("Enter Semester: ")
        u_city = input("Enter City: ")
        
        # We create a dictionary for details
        extra_details = {
            'Branch': u_branch, 
            'Semester': u_sem, 
            'City': u_city
        }
        
        # Calling function
        student_info(u_name, u_roll, *marks_list, **extra_details)
        
        # Check if user wants to continue
        cont = input("\nDo you want to add another student? (y/n): ").lower()
        if cont != 'y':
            print("Exiting Manual Mode...")
            print("=====================================")
            break # Breaks the while loop

else:
    print("Invalid Choice selected.")

#Output Verified
#Exit