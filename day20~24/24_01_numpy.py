# 24_01_numpy.py

import numpy as np

a = np.linspace(0, 10, 10)
print(a)

b = np.linspace(0, 10, 11, dtype=np.float32)  # 10 이하 인 것 주의
print(b)

c = np.int32(b)     # 쉽다!
print(c)

# 퀴즈
# 넘파이 배열을 리스트로 변환하기
d = list(c)
print(d)        # 매개변수로 넘어가는 것이 반복가능한 것이냐가 중요함.
print([i for i in d])

print(c.tolist())
print(c)

# 퀴즈
# 리스트를 넘파이로 바꾸기
e = np.array(d)             # 데이터 타입을 판단하기 힘들 때 쓴다.
print(e)
print(np.int32(d))
print('-'*30)

z1 = np.zeros(5)
z2 = np.zeros([2, 3], dtype=np.int32)
print(z2)
print((np.zeros([2, 3], dtype=int)).dtype)

# 퀴즈
# 1이 들어있는 3행 5열짜리 배열을 만드세요
ones = np.array([1] * 3 * 5).reshape(3, -1)
print(ones)

ones2 = np.zeros([3, 5])+1
print(ones2)

print(np.ones([3, 5], dtype=np.int32))
print()
print(np.full([2, 3], fill_value=-1))   # 원하는 값으로 채우고 싶을 때

print('-'*30)
print(np.random.random(5))

# 균등 vs 정규 분포
# 균등 : 균등함(1/n)
# 정규 : 정규분포 식을 따름
print(np.random.rand(5))            # 균등분포
print(np.random.randn(5))           # 정규분포

print('-'*30)
print(np.random.choice(range(0, 10, 2), 6))     # 범위 안 6개 고르기