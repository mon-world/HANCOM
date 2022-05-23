# 25_02_numpy.py
import numpy as np

a = np.arange(12)
print(a)
print(a[0], a[-1])

b = a.reshape(3, 4)
# 퀴즈
# 2차원 배열의 처음과 마지막 요소를 출력하세요
print(b[0][0], b[-1][-1])
print(b[0, 0], b[-1, -1])   # 이렇게도 가능

# 퀴즈
# 마지막 컬럼 출력
print(b[:, -1])
print(b[::2])

# 퀴즈
# 2차원 배열을 거꾸로 출력하기
print(b[::-1, ::-1])

print('-' * 30)

# 퀴즈
# 0으로 채워진 2차원 배열에서 테두리를 1로 바꾸세요
z = np.zeros([5, 5], dtype=np.int32)
z[0] = 1
z[-1] = 1
z[:,0] = 1
z[:,-1] = 1

# for i in [-1,0]:
#     z[i] = 1
#     z[:,i] = 1

print(z)

# 퀴즈
# 0으로 채워진 2차원 배열에서 속을 2로 바꾸세요
z2 = np.zeros([5, 5], dtype=np.int32)
z2[1:-1, 1:-1] = 2
print(z2)