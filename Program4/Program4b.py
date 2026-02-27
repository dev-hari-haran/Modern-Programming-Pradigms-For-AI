#Hariharan R 128179012
#27-02-26
#Program to implement DataFrame Creation and Access
#Importing Modules
import pandas as pd

#Variable Installation and Setting up Data
nested_dict = {
    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6},
    'Nevada': {2001: 2.4, 2002: 2.9}
}

#Setting up Environment for Processing
#Creating DataFrame (Pandas interprets outer keys as columns, inner as rows)
df = pd.DataFrame(nested_dict)
df.index.name = 'year'
df.columns.name = 'state'

#Accessing 'state' column (Note: In this specific dict, 'Ohio'/'Nevada' are columns)
state_col = df['Ohio'] 

#Output Verified Successfully
print("--- DataFrame ---")
print(df)
print("\nColumns:", df.columns)
print("\n--- 'Ohio' column as Series ---")
print(state_col)
#End