#Hariharan R 128179012
#09-01-2026
#Program to implement a Grade Calculation

#Getting the Mark from user
marks= int(input("Enter your Mark of the subject: "))
if (marks<0 or marks>100):
    marks= int(input("Enter your Mark of the subject: "))
else:
    if (marks >=90):
        print("You got A+ :)")
        print("Try to teach others, you're outstanding")   
    elif (marks < 90 and marks >=80):
        print("You got A :)")
    elif (marks < 80 and marks >=70):
        print("You got B :)")
    elif (marks < 70 and marks >=60):
        print("You got C :)")
    elif (marks < 60 and marks >=50):
        print("You got D :)")
    elif (marks < 50 and marks >=40):
        print("You got P :)")
        print("You want to have a party")   
    elif (marks < 40):
        print("You got F :)")  
        print("Better Luck next time")    
#Output Verified
#End