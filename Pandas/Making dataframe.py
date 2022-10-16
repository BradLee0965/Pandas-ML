import pandas as pd  
import csv

df = pd.read_csv('/Users/Lee/Desktop/GitHub/sideproject-2/AAPL_Historical_Data.csv')

# dict 타입은 순서가 없음. 정렬이 필요
from collections import OrderedDict

df = df[['Date', 'Price', 'High', 'Low', 'Open', 'Change %', 'Vol.']] # 첫번째 방법. 
freinds_ordered_dict = OrderedDict([
    ('name', ['John', 'Nate']),
    ('age', [24, 25]),
    ('job', ['student','teacher'])
])
df2 = pd.DataFrame.from_dict(freinds_ordered_dict) #

print(df2.head)
print(df.head())

friends_list = [['John', 30, 'student'], ['Nate', 35, 'teacher']]
column_name = ['name', 'age', 'job']

df = pd.DataFrame.from_records(friends_list, columns= column_name) # 리스트 데이터를 합쳐서 행렬 만듦. from_records가 핵심.
df.info()



