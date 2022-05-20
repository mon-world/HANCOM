# 23_02_numpy.py

import numpy as np

a = np.arange(12)

# 배열은 같은 데이터만 저장할 수 있다.

# 리스트는 안되고 넘파이는 되는 것 : 차원배열

# 0차원 ~3차원 : [] 갯수 차이


# 퀴즈
# 1차원 ㅐ열을 2차원 배열로 변환하는 코드 만들기
c = np.arange(12)
print(c)

print(np.reshape(c, (3,4)))     # 대괄호로 묶어도 된다. 가독성.
print(c.reshape(3, -1))


# 퀴즈
# 1차원 배열을 3차원 배열로 변환하는 코드 만들기
print(c.reshape(3, 4, -1))
print(c.reshape(-1, 1, 12))


# 퀴즈
# 3차원 배열을 1차원 배열로 변환하는 코드 만들기
d = c.reshape(3, 4, -1)
print(d.reshape(-1))
print(d.reshape(12))
print(np.reshape(d,-1))

print(d.reshape(d.size))
print(d.reshape(d.shape[0]*d.shape[1]*d.shape[2]))