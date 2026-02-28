#Hariharan R 128179012
#27-02-26
#Program to implement Basic Bar Plot
#Importing Modules
import matplotlib.pyplot as plt
import pandas as pd

#Variable Installation
#Series with values [2,4,6,8] and index [a,b,c,d]
s = pd.Series([2, 4, 6, 8], index=['a', 'b', 'c', 'd'])

#Setting up Environment for Processing
#Vertical bar with black color and 0.5 alpha
s.plot.bar(color='k', alpha=0.5)
plt.title("Basic Bar Plot")

#Output Verified Successfully
plt.show()
#End