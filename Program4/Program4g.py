#Hariharan R 128179012
#27-02-26
#Program to implement Concatenation
#Importing Modules
import pandas as pd

#Variable Installation
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

#Setting up Environment for Processing
#Concatenate along index (axis=0)
concat_rows = pd.concat([s1, s2, s3])

#Concatenate along columns (axis=1)
concat_cols = pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])

#Output Verified Successfully
print("--- Concatenated along Index ---")
print(concat_rows)
print("\n--- Concatenated along Columns ---")
print(concat_cols)
#End