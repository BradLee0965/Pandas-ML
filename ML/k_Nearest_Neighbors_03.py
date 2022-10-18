# https://bit.ly/hg-02-2


# 이상한 도미가 하나 있다? 데이터 전처리하는 방법 , 스케일의 중요성

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

import numpy as np

# for , zip 이용하지 않고 numpy 로 행렬 구성해보기 , np.column_stack 사용
# print(np.column_stack([[1,2,3],[4,5,6]]))

fish_data = np.column_stack((fish_length,fish_weight))

# print(fish_data[:5])
# np.ones() , np.zeros() 이용해 정답 데이터 배열 생성
# # np.concatenate 이용해 스칼라 배열 붙이기
# print(np.ones(5),np.zeros(2))
# print(np.concatenate((np.ones(10),np.zeros(3))))
fish_target = np.concatenate((np.ones(35),np.zeros(14)))

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=42)

# 수상한 도미 한마리
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
print(kn.score(test_input, test_target)) # 1이 나옴.

# 수상한 도미 [25,150]
print(kn.predict([[25,150]])) # 0 이나옴. 사이즈는 도미인데 빙어로 판단함. 

import matplotlib.pyplot as plt

# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(25, 150, marker='^')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# kneighbors -> 이웃까지의 거리와 이웃 인덱스 반환. 이웃 샘플 gathering 기본값이 5 이기 때문에 5개 반환
distance , indexes = kn.kneighbors([[25,150]])
print(distance, indexes)


# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(25, 150, marker='^')
# plt.scatter(train_input[indexes,0], train_input[indexes,1])
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

print(train_input[indexes])
print(train_target[indexes])
print(distance)

# 기준 맞추기

# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(25, 150, marker = '^')
# plt.scatter(train_input[indexes,0], train_input[indexes,1])
# plt.xlim(0,1000)
# plt.ylim(0,1000)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

mean = np.mean(train_input, axis = 0)
std = np.std(train_input, axis = 0)
print (mean, std)

new = (([25, 150] - mean)/std)

train_scaled = ((train_input - mean)/ std)
print(train_scaled)

# plt.scatter(train_scaled[:,0], train_scaled[:,1])
# plt.scatter(new[0], new[1] ,marker = '^')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# 기준 맞추고 (브로드 캐스팅 완료) ML 시작

kn.fit(train_scaled, train_target)
test_scaled = ((test_input - mean)/ std)

print(kn.score(test_scaled, test_target)) # 1 나옴.

print(kn.predict([new]))

plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker = '^')
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print(type(train_scaled))