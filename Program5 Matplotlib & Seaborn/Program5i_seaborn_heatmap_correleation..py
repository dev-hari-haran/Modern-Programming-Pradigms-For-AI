#Hariharan R 128179012
#27-02-26
#Program to implement Correlation Heatmap
#Importing Modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#Variable Installation
#DataFrame with random (5x5) data
df = pd.DataFrame(np.random.randn(5, 5), columns=['V1', 'V2', 'V3', 'V4', 'V5'])

#Setting up Environment for Processing
#Compute correlation matrix
corr = df.corr()
#Plot heatmap with annotations
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")

#Output Verified Successfully
plt.show()
#End