#Hariharan R 128179012
#27-02-26
#Program to implement Basic Line Plot
#Importing Modules
import matplotlib.pyplot as plt
import numpy as np

#Variable Installation
#Generating array of 10 numbers from 0 to 9
data = np.arange(10)

#Setting up Environment for Processing
plt.plot(data)
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

#Output Verified Successfully
plt.show()
#End