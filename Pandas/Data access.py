import pandas as pd   
# print(pd.__version__)


# CSV 파일 읽기 및 쓰기

# # CSV : MIME - text/csv

import csv

df = pd.read_csv('/Users/Lee/Desktop/GitHub/sideproject-2/AAPL_Historical_Data.csv')

print(df.shape) # 열과 행의 개수 확인
print(df.head()) # Dataframe 상의 5개 추출
print(df.info()) # row, columns 갯수, 데이터 타입(int : 정수형, object : 문자형, float : 실수형), Missing value (비어있는 값) , 데이터 타입별 칼럼수, 데이터 타입의 용량)
print(df.describe()) # count : Not Nill인 갯수, mean : 전체 데이터 평균, std : 표준편차, min : 최솟값, max : 최댓값 ,사분위범위 (IQR) : 전체 데이터의 50%가 존재하는 구간. 
print(df['Date'].unique()) # 문자형의 'Date' 항목에 들어있는 항목들 확인

# print(df['Vol.'].value_counts()) # 항목에 들어있는 각 데이터의 갯수 추출
print(df.describe().columns.tolist()) # describe()를 이용하여 연속형 columns를 가져온 뒤, columns를 이용하여 숫자 데이터 칼럼의 이름들만 추출해서 가져온다. 그리고 tolist()를 이용하여 그 이름들을 리스트 형태로 만들어 준다. 
a  = df.describe().columns.tolist() # 숫자 데이터 칼럼만 a로 선언.
b = df.columns.tolist() # 전체 칼럼을 리스트로 추출해서 b로 선언.
c = list(set(b)-set(a))# set 이용해서 중복제거
print(c) # 문자형 데이터의 칼럼만 추출.
print(c[0]) # Vol.
print('\'Price\' 값 확인 ' , df['Price'])
print('조건 주기 주가가 100달러 이상인 것만 추출\n', df[df['Price']> 100]) # 조건 주기 주가가 100달러 이상인 것만 추출
print('\'Price\' 총합 확인 :', df['Price'].sum()) # 가격의 총 합
print('평균값 확인 : \n', df.describe().mean())
print('\'Price\' 값 리스트로 나열 :', df['Price'].unique())

print('@@@@@@@@@@@@'*20)

