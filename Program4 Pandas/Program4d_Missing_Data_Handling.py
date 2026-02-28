#Hariharan R 128179012
#27-02-26
#Program to handle Missing Data
#Importing Modules
import pandas as pd
import numpy as np

#Variable Installation
df = pd.DataFrame([[1, np.nan, 3], [4, 5, np.nan], [7, 8, 9]], columns=['A', 'B', 'C'])

#Setting up Environment for Processing
#Drop rows with any NaN
df_dropped = df.dropna()

#Fill NaN with mean of each column
df_filled = df.fillna(df.mean())

#Output Verified Successfully
print("--- Original DataFrame ---")
print(df)
print("\n--- Dropped Rows (dropna) ---")
print(df_dropped)
print("\n--- Filled with Mean (fillna) ---")
print(df_filled)
#End