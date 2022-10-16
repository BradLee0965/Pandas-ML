import pandas as pd 
import numpy as np
a = [1,2,3]
print('Structure of a :')
print(pd.Series(a)) # 1차원 Series 구조
b = {'name' : ['leeseungho', 'moonseonghee'], 'age' : [30, 29], 'weight' : [70, 60]}
print('Structure of b :\n', pd.DataFrame(b))
