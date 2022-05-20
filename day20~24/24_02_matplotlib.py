# 24_02_matplotlib.py

import matplotlib.pyplot as plt
import numpy as np

def plot_1():
    plt.plot([1, 2, 3, 4, 5], [10, 20, 30, 40, 50], 'k')    # k가 블랙
    plt.show()                      # 있어야 그래프 표시

# 퀴즈
# y = x ^ 2 그래프를 그려주세요
def plot_2(x):
    # plt.plot(x,[i**2 for i in x])
    # plt.show()

    # a, b = [], []
    # for i in range(-10, 11):
    #     a.append(i)
    #     b.append(i*i)
    #
    # plt.plot(a, b, 'ro')
    # plt.show()

    plt.plot(x, x**2, 'ro')
    plt.show()
x = np.linspace(0, 10, 100)


# 퀴즈
# desmos 사이트에서 그렸던 로그 그래프 4개를 그려주세요
def plot_4(x):
    plt.plot(x, np.log(x))
    plt.plot(-x, np.log(x))
    plt.plot(x, -np.log(x))
    plt.plot(-x, -np.log(x))

    plt.show()
x = np.arange(0.1, 3, 0.1)

# TypeError: subplots() takes from 0 to 2 positional arguments but 3 were given
def plot_5():
    x = np.arange(0.01, 2, 0.01)

    plt.subplots(1, 2, 1)
    plt.grid()
    plt.plot(x, np.log(x))
    plt.plot(x, -np.log(x))

    plt.figure()
    plt.subplots(2, 2, 2)
    plt.plot(-x, np.log(x))
    plt.plot(-x, -np.log(x))

    plt.show()



# 퀴즈
# 남여 데이터를 같은 공간에 표시
def plot_6():
    men = [25, 15, 30, 20, 40]
    women = [35, 50, 10, 25, 40]

    indices = np.arange(len(men))

    plt.bar(indices-0.2, men, color='b', width=0.4)     # 이동함
    plt.bar(indices+0.2, women, color='r', width=0.4)

    plt.show()





# plot_2(x)
# plot_4(x)
# plot_5()
plot_6()






