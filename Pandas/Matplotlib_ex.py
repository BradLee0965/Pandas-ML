import pandas as pd  
from matplotlib import pyplot as plt  


import csv

df = pd.read_csv('/Users/Lee/Desktop/GitHub/sideproject-2/AAPL_Historical_Data.csv')
plt.bar(df['Date'], df['Price'])
plt.show()