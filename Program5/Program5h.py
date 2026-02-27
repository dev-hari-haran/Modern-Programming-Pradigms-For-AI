#Hariharan R 128179012
#27-02-26
#Program to implement Pairplot with KDE
#Importing Modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#Variable Installation
#4 columns of random data
trans_data = pd.DataFrame(np.random.randn(100, 4), 
                          columns=['macro', 'tips', 'comp1', 'comp2'])

#Setting up Environment for Processing
#Pairplot with KDE on diagonal
#Note: Seaborn pairplot generates its own figure and titles
sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})

#Output Verified Successfully
plt.show()
#End
