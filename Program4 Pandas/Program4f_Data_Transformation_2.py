#Hariharan R 128179012
#27-02-26
#Program to implement DataFrame Merging
#Importing Modules
import pandas as pd

#Variable Installation
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a'], 'data1': range(5)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

#Setting up Environment for Processing
merged_df = pd.merge(df1, df2, on='key', how='inner')

#Output Verified Successfully
print("--- Merged DataFrame (Inner Join) ---")
print(merged_df)
#End