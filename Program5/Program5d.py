#Hariharan R 128179012
#27-02-26
#Program to implement Stacked Horizontal Bar Plot
#Importing Modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Variable Installation
#DataFrame with random (3x4) values
df = pd.DataFrame(np.random.rand(3, 4), 
                  index=['One', 'Two', 'Three'], 
                  columns=['A', 'B', 'C', 'D'])

#Setting up Environment for Processing
#Stacked horizontal bar with alpha 0.5
df.plot.barh(stacked=True, alpha=0.5)
plt.title("Stacked Bar Plot")
plt.legend(loc='best')

#Output Verified Successfully
plt.show()
#End