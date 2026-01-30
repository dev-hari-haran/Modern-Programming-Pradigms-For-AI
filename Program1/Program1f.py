#Start
#Hariharan R
#23-01-2026
#Program for Menu Driven String Manipulation: Case, Count, Reverse, Replace

while True: # While Statement
    print("\n===== STRING MENU =====")
    print("1. Convert to Uppercase")
    print("2. Convert to Lowercase")
    print("3. Convert to Title Case")
    print("4. Check Palindrome")
    print("5. Count Number of Words")
    print("6. Reverse the String")
    print("7. Replace Text")
    print("8. Exit")
    
    #Enter the Choices
    choice = input("Enter your choice (1-8): ")

    if choice == '8': #Exiting the Program
        print("Exiting program... Goodbye!")
        break

    if choice not in ['1', '2', '3', '4', '5', '6', '7']: #Invalid Choices
        print("Invalid choice! Breaking the loop.")
        break

    # Take string input from user
    text = input("Enter a string: ")

    if choice == '1': #Uppercase
        print("Result:", text.upper())
        
    elif choice == '2': #Lowercase
        print("Result:", text.lower())
        
    elif choice == '3': #Title Case
        print("Result:", text.title())
        
    elif choice == '4': #Palindrome Check
        reversed_text = text[::-1]
        if text.lower() == reversed_text.lower():
            print("The string", text, "is a Palindrome.")
        else:
            print("The string", text, "is NOT a Palindrome.")

    elif choice == '5': #Count Number of Words
        # split() breaks the string into a list of words based on spaces
        words = text.split()
        print("Total number of words:", len(words))

    elif choice == '6': #Reverse the String
        # Slicing with -1 step reverses the whole string
        print("Reversed String:", text[::-1])

    elif choice == '7': #Replace occurrences
        old_str = input("Enter the text to find: ")
        new_str = input("Enter the text to replace it with: ")
        # replace() swaps all occurrences of the old string with the new one
        print("Updated String:", text.replace(old_str, new_str))

#Output Verified
#Exit