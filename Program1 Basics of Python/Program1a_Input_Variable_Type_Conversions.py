#Hariharan R 128179012
#09-01-26
#Program to implement a basics of python
#Importing Modules
from tabulate import tabulate

#Variable Installation and geting Input 
#Name
Name= input(" Enter your name: ")
#Roll Number
Roll = int(input("Enter the Roll Number: "))
#Marks
#Marks for Python
Marks_Python = float(input("Enter the Mark for Python: "))
#Marks for Mathematics
Marks_Maths = float(input("Enter the Mark for Mathematics: "))

#Setting up Environment for Processing
#Calculating the Total Marks
Total_Marks = Marks_Python + Marks_Maths
#Calculating Percentage
Percentage = (Total_Marks/200)*100

#Assigning the data to tabulate form
data = [
    ["Name", "String", Name],
    ["Roll Number", "Integer", Roll],
    ["Marks_Python","Float", Marks_Python ],
    ["Marks_Mathematics","Float", Marks_Maths ],
    ["Total","Float", Total_Marks ],
    ["Percentage","Float", Percentage*100,"%"]
]
#Assigning the Header
headers = ["Variable", "Datatype", "Value"]
#Presenting the Data in Tabulate Form
print(tabulate(data, headers=headers, tablefmt="grid"))
#Output Verified Sucessfully
#End