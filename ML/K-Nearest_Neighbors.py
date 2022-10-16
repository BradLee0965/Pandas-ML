# 생선분류 문제 (도미와 빙어 구분)
# k-최근접 이웃 분류 모델 사용
# scikit-learn 사용
####################
# 도미
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
# 빙어
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

import matplotlib.pyplot as plt

# plt.scatter(bream_length, bream_weight)
# plt.scatter(smelt_length, smelt_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()
length = bream_length + smelt_length
weight = bream_weight + smelt_weight

fish_data = [[l,w] for l,w in zip(length, weight)] # 도미 + 빙어 데이터 합쳐서 하나의 리스트로 만듦

print(fish_data)
print(len(bream_length)) # 도미 데이터는 35개 
fish_target = [1] * 35 + [0] * 14 # 도미 데이터만 1로 반환, 나머지는 0 (여기서 나머지는 빙어밖에 없음)

print(fish_target)

from sklearn.neighbors import KNeighborsClassifier


kn = KNeighborsClassifier() # K- 최근접 이웃 모델 소환, 변수로 설정.
kn.fit(fish_data, fish_target) # 훈련에 사용할 특성 + 정답 데이터(1,0)을 전달함. 클래스 기본값은 5 , 즉 주위 데이터 다섯개만 보고 1인지 0 인지 판단하겠다는 말. 기본값을 확장시키면 더 많은 주위데이터를 본다.
print(kn.score(fish_data, fish_target)) # scikit-learn 모델의 성능 측정 (0~1.0)


# k- 최근접 이웃 알고리즘 

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.scatter(30, 600, marker = '^') 
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print(kn.predict([[30,600]])) # 이 값은 정답일까 ?
print(kn._fit_X) # fit의 x속성 --> fish_data 값
print(kn._y) # fish_target 값

kn49 = KNeighborsClassifier(n_neighbors=49) # 주위 데이터를 49개 보겠다. 즉 다 보겠다. 
kn49.fit(fish_data, fish_target)

print(kn49.score(fish_data, fish_target)) # 이때의 성능은 35(도미 데이터)/ 49(전체 데이터) 이다 
print(35/49)