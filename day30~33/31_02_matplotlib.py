# 31_02_matplotlib.py
import matplotlib.pyplot as plt
from matplotlib import cm           # color map
import numpy as np


def colormap_1():
    x = np.random.rand(100)
    y = np.random.rand(100)
    # print(x)

    # plt.plot(x, y, 'ro')      # 산점도 minimal 버전
    # plt.scatter(x, y)         # 산점도 full 버전

    t = np.arange(len(x))
    # t = np.arange(len(x) // 2)    # 100개가 아니어서 에러
    # t = np.arange(len(x) * 2)     # 100개가 아니어서 에러
    # plt.scatter(x, y, c=t)
    # plt.scatter(x, y, c=t, cmap='jet')

    # 퀴즈
    # 산점도를 두 가지 색상으로 그려보세요
    # plt.scatter(x, y, c=[t[0]] * 50 + [t[-1]] * 50, cmap='jet')

    print(t[[0, -1]] * 50)
    print(list(t[[0, -1]]) * 50)
    plt.scatter(x, y, c=list(t[[0, -1]]) * 50, cmap='jet')

    plt.show()


# 퀴즈
# 대각선 산점도를 그려보세요 (위쪽 노랑, 아래쪽 보라)
def colormap_2():
    x = np.arange(100)

    plt.figure(figsize=[10, 5])

    plt.subplot(1, 4, 1)
    # (0, 0) (1, 1) ...
    plt.scatter(x, x, c=x)

    # (0, 99) (1, 98) ...
    plt.scatter(x, x[::-1], c=x)

    plt.subplot(1, 4, 2)
    plt.scatter(x, x, c=x)
    plt.scatter(x, x[::-1], c=x[::-1])  # ::-1 -> 99 ~ 0

    plt.subplot(1, 4, 3)
    plt.scatter(x, x, c=x)
    plt.scatter(x, x[-1]-x, c=-x)       # 0(마지막 색상) ~ -99(처음 색상)

    plt.subplot(1, 4, 4)
    plt.scatter(x, x, c=x)
    # plt.scatter(x, list(reversed(x)), c=x)
    plt.scatter(x, np.flip(x), c=x, cmap='viridis_r')

    # print(cm.get_cmap().name)         # viridis, 현재 컬러맵 이름 구하기

    plt.tight_layout()
    plt.show()


def colormap_3():
    print(len(plt.colormaps()))         # 166
    print(plt.colormaps())
    # ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r',
    # 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r',
    # 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r',
    # 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r',
    # 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r',
    # 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r',
    # 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r',
    # 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r',
    # 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r',
    # 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r',
    # 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r',
    # 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r',
    # 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r',
    # 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r',
    # 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r',
    # 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r',
    # 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r',
    # 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

    # 퀴즈
    # 여러분이 좋아할 것 같은 이름의 컬러맵을 아래 코드에 적용해 보세요
    x = np.arange(100)

    plt.figure(figsize=[10, 5])

    plt.subplot(1, 4, 1)
    plt.scatter(x, x, c=x, cmap='summer')
    plt.title('summer')

    plt.subplot(1, 4, 2)
    plt.scatter(x, x, c=x, cmap='Blues')
    plt.title('Blues')

    plt.subplot(1, 4, 3)
    plt.scatter(x, x, c=x, cmap='inferno')
    plt.title('inferno')

    plt.subplot(1, 4, 4)
    plt.scatter(x, x, c=x, cmap='terrain')
    plt.title('terrain')

    plt.tight_layout()
    plt.show()


def colormap_4():
    plasma = plt.get_cmap('plasma')

    # 컬러맵은 256개의 색상으로 구성
    print(plasma(-1))       # (0.050383, 0.029803, 0.527975, 1.0)
    print(plasma(0))        # (0.050383, 0.029803, 0.527975, 1.0)   RGBA
    print(plasma(255))      # (0.940015, 0.975158, 0.131326, 1.0)
    print(plasma(256))      # (0.940015, 0.975158, 0.131326, 1.0)
    print()

    # if c < 0:
    #     c = 0
    # if c > 255:
    #     c = 255

    # 퀴즈
    # 플라즈마 컬러맵의 정가운데 색상을 출력하세요 (2가지)
    print(plasma(0.0))
    print(plasma(1.0))
    print()

    print(plasma(127))          # 정가운데 아님
    print(plasma(128))
    print(plasma(0.5))
    print()

    print(plasma(127 / 255))    # 정가운데 아님
    print(plasma(128 / 255))
    print()

    print(plasma(0), plasma(255))
    print(plasma([0, 255]))
    print(plasma(range(0, 256, 64)))
    print(plasma(np.linspace(0, 1, 5)))


# colormap_1()
# colormap_2()
# colormap_3()
colormap_4()






