# 34_03_preprocessing.py

from sklearn import preprocessing
import numpy as np

x = [[4 ,5],
     [6, 7],
     [8, 9]]
x = np.array(x)
print(preprocessing.add_dummy_feature(x))

# 퀴즈
# 첫 행에 더미 피처 추가
print(preprocessing.add_dummy_feature(x.T).T)

def Binarizer():
     x = [[-1, -1, 2],
          [3, -2, -2],
          [-2, 3, 0]]

     bin_1 = preprocessing.Binarizer()       # 이 데이터를 다른 데이터로 변환환
     # bin_1.fit(x)
     # print(bin_1.transform(x))

     print(bin_1.fit_transform(x))           # 두 줄 한 번에 처리

     bin_2 = preprocessing.Binarizer().fit(x)     # 파이썬적 표현

Binarizer()