import pandas as pd  
from matplotlib import pyplot as plt  


import csv

df = pd.read_csv('/Users/Lee/Desktop/python/GitHub/sideproject/AAPL_Historical_Data.csv')
plt.bar(df['Date'], df['Price'])
plt.show()