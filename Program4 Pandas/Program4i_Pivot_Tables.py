#Hariharan R 128179012
#27-02-26
#Program to implement Pivot and Pivot Tables
#Importing Modules
import pandas as pd

#Variable Installation
data = pd.DataFrame({
    'date': ['2026-01-01', '2026-01-01', '2026-01-02', '2026-01-02'],
    'item': ['apple', 'orange', 'apple', 'orange'],
    'value': [10, 15, 12, 18]
})

#Setting up Environment for Processing
#Using pivot()
pivoted = data.pivot(index='date', columns='item', values='value')

#Using pivot_table() for aggregation
pivoted_table = data.pivot_table(values='value', index='date', columns='item', aggfunc='mean')

#Output Verified Successfully
print("--- Reshaped using pivot() ---")
print(pivoted)
print("\n--- Aggregated using pivot_table() ---")
print(pivoted_table)
#End
#Output
