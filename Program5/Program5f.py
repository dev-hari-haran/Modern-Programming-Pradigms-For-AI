#Hariharan R 128179012
#27-02-26
#Program to implement Distribution Plot
#Importing Modules
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Variable Installation
#1000 random normal numbers
data = np.random.randn(1000)

#Setting up Environment for Processing
#histplot with KDE density in black
sns.histplot(data, kde=True, color='black')
plt.title("Distribution Plot")

#Output Verified Successfully
plt.show()
#End