#Hariharan R 128179012
#27-02-26
#Program to implement Bar Plot with Means
#Importing Modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Variable Installation
#Simulated tips dataset
tips = pd.DataFrame({
    'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
    'day': ['Sun', 'Sun', 'Sun', 'Sat', 'Sat']
})

#Setting up Environment for Processing
#Plot mean total_bill by day
sns.barplot(x='day', y='total_bill', data=tips)
plt.title("Bar Plot with Means")

#Output Verified Successfully
plt.show()
#End