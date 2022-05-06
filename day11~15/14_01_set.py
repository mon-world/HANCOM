# 14_01_set.py

import random

def make_randoms(size):
    a = []
    for _ in range(size):
        a.append(random.randrange(10))

    return a


# 퀴즈
# 1차원 리스트에 포함된 숫자들의 빈도를 구하세요
random.seed(23)
ns = make_randoms(100)
print(ns)

def fq():
    # counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(len(ns)):
    #     if   ns[i] == 0: counts[0] += 1
    #     elif ns[i] == 1: counts[1] += 1
    #     elif ns[i] == 2: counts[2] += 1
    #     elif ns[i] == 3: counts[3] += 1
    #     elif ns[i] == 4: counts[4] += 1
    #     elif ns[i] == 5: counts[5] += 1
    #     elif ns[i] == 6: counts[6] += 1
    #     elif ns[i] == 7: counts[7] += 1
    #     elif ns[i] == 8: counts[8] += 1
    #     else        : counts[9] += 1
    #
    # print(counts)

    # counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(len(ns)):
    #     for j in range(10):
    #         if ns[i] == j: counts[j] += 1
    #         break

    # 더 쉽게 정리하기
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for n in ns:
        counts[n] += 1
        # if   n == 0: counts[n] += 1
        # elif n == 1: counts[n] += 1
        # elif n == 2: counts[n] += 1
        # elif n == 3: counts[n] += 1
        # elif n == 4: counts[n] += 1
        # elif n == 5: counts[n] += 1
        # elif n == 6: counts[n] += 1
        # elif n == 7: counts[n] += 1
        # elif n == 8: counts[n] += 1
        # else       : counts[n] += 1

    print(counts)

fq()

# 퀴즈
# 리스트에 들어있는 숫자들 중에서 중복된 숫자를 제거하세요
# set과 dictionary : 빨리 찾기위해 사용
s = set(ns)
print(s)
# print(s[0])   # 에러

s = list(s)
print(s)

