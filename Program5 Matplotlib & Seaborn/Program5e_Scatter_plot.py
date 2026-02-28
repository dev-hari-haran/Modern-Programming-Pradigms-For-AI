#Hariharan R 128179012
#27-02-26
#Program to implement Basic Scatter Plot
#Importing Modules
import matplotlib.pyplot as plt
import numpy as np

#Variable Installation
#x as arange(30), y as x + random
x = np.arange(30)
y = x + np.random.randn(30) * 3

#Setting up Environment for Processing
#Scatter with blue color and alpha 0.3
plt.scatter(x, y, color='blue', alpha=0.3)
plt.title("Basic Scatter Plot")

#Output Verified Successfully
plt.show()
#End