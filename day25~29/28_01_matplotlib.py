# 28_01_matplotlib.py

# 퀴즈
# 0 +1 -1로 변하는 100일 동산 주식 차트 시뮬레이션

import numpy as np
import random
import matplotlib.pyplot as plt

# a = np.random.randint(100, size=99)
#
# x = [i % 3 for i in a]
# x = np.array(x) - 1
# print(x)
#
# x_sum = []
# x_0 = 0
# for i in x:
#     x_0 += i
#     x_sum.append(x_0)
#
#
# indices = np.arange(len(x_sum))
#
# plt.bar(indices, x_sum, color='b')
# plt.show()

# 더 좋은 예. randrange 함수 사용
def random_walker_1():
    pos = 0
    x, y = [], []
    for i in range(1000):
        v = random.randrange(-1, 2)
        pos += v
        # print(pos, v)

        x.append(i)
        y.append(pos)

    plt.plot(x, y, 'b')
    plt.show()

def random_walker_2():
    x = range(100)
    # y = np.random.choice([-1, 0, 1], len(x))
    y = np.random.randint(0, 3, len(x))
    y -= 1
    y[0] = 0

    print(list(np.cumsum(y)))   # 아래보다 훨씬 빠름. 바로계산.
    # y = [sum([y[:i+1]]) for i in range(len(x))]
    y = np.cumsum(y)

    plt.plot(x, y, 'b')
    plt.show()

random_walker_2()