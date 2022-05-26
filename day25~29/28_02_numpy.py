# 28_02_numpy.py

import numpy as np

# 퀴즈
# 2차원 배열을 전치 형태로 출력하기
c = np.arange(12).reshape(4, 3)
d = np.zeros([len(c[0]), len(c[:,0])])
print(c)
print(c[0])
for i in range(len(c[:,0])):
    for j in range(len(c[0])):
        d[j][i] = c[i][j]

print(d)

print(c.T)