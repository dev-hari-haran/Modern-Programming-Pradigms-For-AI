#Hariharan R 128179012
#27-02-26
#Program to implement Indexing and Slicing
#Importing Modules
import pandas as pd
import numpy as np

#Variable Installation
#Series Creation
ser = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])

#DataFrame Creation
df = pd.DataFrame(np.arange(16).reshape((4, 4)),
                  index=['Ohio', 'Colorado', 'Utah', 'New York'],
                  columns=['one', 'two', 'three', 'four'])

#Setting up Environment for Processing
#Selection using loc (labels)
ser_sliced = ser.loc['b':'d']

#Selection using iloc (integers)
df_sliced = df.iloc[1:3, 0:2]

#Output Verified Successfully
print("--- Series Slicing (loc 'b':'d') ---")
print(ser_sliced)
print("\n--- DataFrame Slicing (iloc rows 1-2, cols 0-1) ---")
print(df_sliced)
#End