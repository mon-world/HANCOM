# 19_01_comprehension.py

import random
import re

# 퀴즈
# 2차원 리스트에서 가장 큰 숫자를 찾아주세요
random.seed(41)
c1 = [random.randrange(100) for _ in range(10)]
c2 = [random.randrange(100) for _ in range(10)]
c3 = [random.randrange(100) for _ in range(10)]

c = [c1, c2, c3]
print(*c, sep='\n', end='\n\n')

print([n for d in c for n in d])
print(max([n for d in c for n in d]))

print([max(d) for d in c])
print(max([max(d) for d in c]))
print('-' * 30)

# 퀴즈
# 10000보다 작은 양수에 들어있는 8의 갯수를 구하세요 (구글 입사 문제)
# 808 -> 2
eights = 0
for n in range(10000):
    for c in str(n):
        # print(c)
        if c == '8':
            eights += 1

print(eights)

eights = []
for n in range(10000):
    for c in str(n):
        # print(c)
        if c == '8':
            eights.append(c)

print(len(eights))

eights = []
for n in range(10000):
    for c in str(n):
        # print(c)
        eights.append(c == '8')

print(sum(eights))

# 한 줄 표시
print(len([c for n in range(10000) for c in str(n) if c == '8']))


def eight_count(n):
    cnt = 0
    for c in str(n):
        cnt += (c == '8')
    return cnt
