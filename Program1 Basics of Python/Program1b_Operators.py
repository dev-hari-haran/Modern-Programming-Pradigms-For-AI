#Hariharan R 128179012
#09-01-2026
#Program to implement a python operators

#Getting the data from user
a = int(input("Enter the value of A: "))
b = int(input("Enter the Value of B: "))

#Setting up the Environment for Processing
#Performing Operator Functions
#Printing Values of a and b using Arithmetic Operators

print("Arithmetic Operators")
print("Operator 1 - '+': A + B:",a+b)
print("Operator 2 - '-': A - B:",a-b)
print("Operator 3 - '*': A * B:",a*b)
print("Operator 4 - '/': A / B:",a/b)
print("Operator 5 - '//': A // B:",a//b)
print("Operator 6 - '%': A % B:",a%b)
print("Operator 7 - '**': A ** B:",a**b)

#Printing Values of a and b using Relation Operators
print("Relation Operators")
print("Operator 1 - '>': A>B:", a>b)
print("Operator 2 - '<': A<B:", a<b)
print("Operator 3 - '<=': A<=B:", a<=b)
print("Operator 4 - '>=': A>=B:", a>=b)
print("Operator 5 - '==': A==B:", a==b)
print("Operator 6 - '!=': A!=B:", a!=b)


#Printing Values of a and b using Logical Operators
print("Operator 1 - 'AND': A>10 and B>10:", a>10 and b>10)
print("Operator 2 - 'OR': A>10 or B>10:", a>10 or a>10)
print("Operator 3 - 'NOT': A is NOT Greater than 10:")
#Conditional Statement for NOT Operator
if not a >10:
    print(False)
else:
    print(True)

#Printing Values of a and b using Bitwise Operators
print("Bitwise Operators")
# Operator 1: AND (&) - Sets each bit to 1 if both bits are 1
print("Operator 1 - '&' (AND):  A & B  =", a & b)
# Operator 2: OR (|) - Sets each bit to 1 if one of two bits is 1
print("Operator 2 - '|' (OR):   A | B  =", a | b)
# Operator 3: XOR (^) - Sets each bit to 1 if only one of two bits is 1
print("Operator 3 - '^' (XOR):  A ^ B  =", a ^ b)
# Operator 4: NOT (~) - Inverts all the bits (Formula: -(n+1))
print("Operator 4 - '~' (NOT):  ~A     =", ~a)
# Operator 5: Zero fill left shift (<<) - Shift left by pushing zeros in from the right
print("Operator 5 - '<<' (LS):  A << 2 =", a << 2)
# Operator 6: Signed right shift (>>) - Shift right by pushing copies of the leftmost bit
print("Operator 6 - '>>' (RS):  A >> 2 =", a >> 2)
#Output Verified
#End


