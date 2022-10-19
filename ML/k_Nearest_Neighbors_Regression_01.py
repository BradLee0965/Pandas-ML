# https://bit.ly/hg-03-1

# 회귀(regression)은 문제의 분류가 아니라 임의의 수치를 예측하는 문제. 결정계수 값(R^2)을 반환함.

import numpy as np
import matplotlib.pyplot as plt




perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 
     1000.0, 1000.0]
     )

plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()



# test_array = np.array([1,2,3,4])
# print(test_array)
# test_array = test_array.reshape(-1,1)
# print(test_array)

print(perch_length.shape)
# 2차원 행렬로 변환
perch_length = perch_length.reshape(-1,1)
print(perch_length.shape)
perch_weight = perch_weight.reshape(-1,1)
print(perch_weight.shape)

# 결정계수 (R^2)
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)

# print(type(perch_length), type(test_input))


from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor()

knr.fit(train_input, train_target)

print(knr.score(test_input, test_target))

# R^2 의 실제 값 차이를 볼수 있음. (평균으로) --> mean_absolute_error
test_prediction = knr.predict(test_input)

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(test_target, test_prediction)
print(mae) # 타겟값과 예측값의 차이가 19g 평균 정도임 

print(knr.score(train_input, train_target))
 # 훈련세트의 결정계수가 더 작다 --> 과소적합 --> k 개수 줄여서 더 복잡하게 만들어야 함. 
knr.n_neighbors = 3

knr.fit(train_input, train_target)
print(knr.score(train_input, train_target))
print(knr.score(test_input, test_target)) # 테스트 세트의 R^2 이 살짝 더 낮게 나옴 --> 모델링이 제대로 됨.
  
 
 
