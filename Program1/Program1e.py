#Start
#Hariharan R
#Functions for Prime Check and Factorial
import math

def is_prime(n):
    """
    Checks if a number is prime using trial division up to the square root.
    """
    # 0, 1, and negative numbers are not prime
    if n <= 1:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # Exclude all other even numbers
    if n % 2 == 0:
        return False
    
    # Check only odd numbers up to the square root of n
    # We use int(math.sqrt(n)) + 1 for the range boundary
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
            
    return True

def factorial(n):
    #Calculates the factorial of a non-negative integer n iteratively.

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example Usage 
#Prime Check 
number_to_check = int(input("Enter the Number to check for a Prime Number: "))
if is_prime(number_to_check):
    print(number_to_check, "is a prime number.")
else:
    print(number_to_check, "is not a prime number.")


fact_num = int(input("Enter the number to check factorial: "))
print("The factorial of", fact_num, "is:", factorial(fact_num))
#Output Verified
#Exit