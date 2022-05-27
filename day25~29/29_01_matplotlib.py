# 29_01_matplotlib.py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

def show_b():
    print(plt.style.available)
    print(len(plt.style.available))

    x = np.linspace(1, 10)
    print(x.shape)

    with plt.style.context('fivethirtyeight'):
        plt.plot(x, np.log(x), 'rx')
        plt.plot(x, np.sin(x))

    plt.show()

# 퀴즈
# 26가지 스타일 5행 6열로 이루어진 피겨 1개에 그려주세요
def show_style():
    x = np.linspace(1, 10)

    plt.figure(figsize=[15, 10])    # 새로운 피겨를 만들어줌
    for i, style in enumerate(plt.style.available, 1):

        plt.subplot(5, 6, i)

        with plt.style.context(style):
            plt.plot(x, np.log(x), 'rx')
            plt.plot(x, np.sin(x))

    plt.tight_layout()      # 주변 여백 사라짐.
    plt.show()
    # plt.savefig('data/plt_styles.png')      # 저장

# 막대그래프
def show_style_2():
    x = np.arange(10)
    y = x + np.random.randint(-5, 6, len(x))

    plt.figure(figsize=[15, 10])  # 새로운 피겨를 만들어줌
    for i, style in enumerate(plt.style.available, 1):
        with plt.style.context(style):
            plt.subplot(5, 6, i)
            plt.bar(x, y, color=colors.TABLEAU_COLORS)

    plt.tight_layout()
    plt.show()

# 퀴즈
# 막대그래프 2개를 추가해서 나머지 빈칸 채우기
def show_subplots():
    x = np.arange(10)
    y = x + np.random.randint(-5, 6, len(x))

    # 전체칸을 3x3으로 나누고, 0,0에서 시작하는데 컬럼을 2개로 설정한다...?
    ax1 = plt.subplot2grid([3, 3], [0, 0], colspan=2)
    ax2 = plt.subplot2grid([3, 3], [1, 0], rowspan=2)
    ax3 = plt.subplot2grid([3, 3], [1, 1], rowspan=2, colspan=2)
    ax4 = plt.subplot2grid([3, 3], [0, 2])

    ax1.plot(x, y, 'r')
    ax2.plot(x, y, 'gd')
    ax3.bar(x, y, color=colors.TABLEAU_COLORS)
    ax4.bar(x, y)

    plt.show()
    # plt.savefig('data/plt_styles.png')      # 저장


# show_style()
# show_style_2()
show_subplots()

print(np.linspace(1,10))

