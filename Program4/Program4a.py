#Hariharan R 128179012
#27-02-26
#Program to implement Pandas Series Basics
#Importing Modules
import pandas as pd
import numpy as np

#Variable Installation and Setting up Data
data_dict = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

#Setting up Environment for Processing
#Creating Series
obj = pd.Series(data_dict)

#Printing Series details
print("--- Original Series ---")
print(obj)
print("\nIndex:", obj.index)
print("Values:", obj.values)

#Adding new state 'California' with NaN
obj['California'] = np.nan

#Checking for missing data
missing_data = obj.isna()

#Output Verified Successfully
print("\n--- Series with California ---")
print(obj)
print("\n--- Missing Data Check (isna) ---")
print(missing_data)
#End