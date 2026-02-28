#Hariharan R 128179012
#27-02-26
#Program to implement Grouping and Aggregation
#Importing Modules
import pandas as pd
import numpy as np

#Variable Installation
df = pd.DataFrame({
    'key1': ['a', 'a', 'b', 'b', 'a'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': np.random.randn(5),
    'data2': np.random.randn(5)
})

#Setting up Environment for Processing
#Group by key1 and compute mean
mean_group = df.groupby('key1').mean(numeric_only=True)

#Group by both keys and sum
sum_group = df.groupby(['key1', 'key2']).sum()

#Output Verified Successfully
print("--- Mean by key1 ---")
print(mean_group)
print("\n--- Sum by key1 and key2 ---")
print(sum_group)
#End