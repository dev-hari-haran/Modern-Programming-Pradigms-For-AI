#Start
#Hariharan R 
#23-01-2026
#Program to Menu Driven Calculator
# Menu Driven Calculator with Loop Control

while True: # While Statement
    print("\n===== MENU =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    #Enter the Choices
    choice = input("Enter your choice (1-5): ")
    
    if choice == '5':#Exiting the Program
        print("Exiting program... Goodbye!")
        break
    
    if choice not in ['1', '2', '3', '4']: #Invalid Choices
        print("Invalid choice! Breaking the loop.")
        break
    
    # Take two numbers from user
    try:#Float Value
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError: #Value Error Statement
        print("Invalid input! Numbers only. Breaking the loop.")
        break
    
    if choice == '1': #Addition
        print("Result:", num1, "+", num2, "=", num1 + num2)
    elif choice == '2': #Subtraction 
        print("Result:", num1, "-", num2, "=", num1 - num2)
    elif choice == '3': #Multiply 
        print("Result:", num1, "*", num2, "=", num1 * num2)
    elif choice == '4': #Dividion 
        if num2 == 0:
            print("Error: Division by zero is not allowed!") #Zero Error
        else:
            print("Result:", num1, "/", num2, "=", num1 / num2) 

#Output Verified
#Exit