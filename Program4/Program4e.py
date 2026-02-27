#Hariharan R 128179012
#27-02-26
#Program to implement Data Transformation via Map
#Importing Modules
import pandas as pd

#Variable Installation
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'pastrami']})
meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow'
}

#Setting up Environment for Processing
data['animal'] = data['food'].map(meat_to_animal)

#Output Verified Successfully
print("--- Transformed DataFrame ---")
print(data)
#End