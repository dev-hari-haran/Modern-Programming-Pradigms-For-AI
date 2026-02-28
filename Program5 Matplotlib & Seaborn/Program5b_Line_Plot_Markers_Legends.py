#Hariharan R 128179012
#27-02-26
#Program to implement Line Styles Comparison
#Importing Modules
import matplotlib.pyplot as plt
import numpy as np

#Variable Installation
#30 random numbers with cumsum
data1 = np.random.randn(30).cumsum()
data2 = np.random.randn(30).cumsum()
data3 = np.random.randn(30).cumsum()

#Setting up Environment for Processing
plt.plot(data1, label='Default')
plt.plot(data2, 'k--', marker='o', label='Dashed with Markers')
plt.plot(data3, 'k:', label='Dotted')

plt.title("Line Styles Comparison")
plt.legend(loc='best')

#Output Verified Successfully
plt.show()
#End