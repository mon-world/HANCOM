# 27_01_matplotlib.py

import matplotlib.pyplot as plt
import numpy as np

# 퀴즈
# 2016_GDP.txt 파일을 읽어서 반환하는 함수 만들기

# 아래 코드는 칼럼 구분을 못하기 때문에 좋지 않음.
# def read_file():
#     with open('data/2016_GDP.txt', 'r', encoding='utf-8') as f:
#         return list(f)
#
# rows = read_file()
# print('\n'.join(rows))

# q1. 1을 01로 못바꾸나?

# 아래 코드는 리스트 활용
# def read_file1(file):
#     x = []
#     with open(file, 'r', encoding='utf-8') as f:
#         for line in f:
#             x.append(line.strip().split(':'))   # strip을 써야 \n 안생김
#     return x
# rows = read_file1('data/2016_GDP.txt')
# print(*rows, sep='\n')


def read_file(file):
    f = open(file, 'r', encoding='utf-8')

    # header 스킵하기
    f.readline()
    # 1번 : 따로 출력
    #
    # countries, dollars = [], []
    # for line in f:
    #     # print(line.strip().split(':'))
    #     # 1. 달러의 , 삭제하기
    #     # 2. 달러의 dtpye 바꾸기
    #     rank, country, dollar = line.strip().split(':')
    #
    #     countries.append(country)
    #     dollars.append(int(dollar.replace(',', '')))
    # f.close()
    #
    # return countries, dollars

    # 2번 : 묶어서 리턴하기
    gdp = []

    for line in f:

        rank, country, dollar = line.strip().split(':')
        dollar = int(dollar.replace(',', ''))

        gdp.append(([country, dollar]))
    f.close()

    return gdp


rows = np.array(read_file('data/2016_GDP.txt'))
print(rows[:10, 0])

# 퀴즈
# read_gdp가 반환한 데이터에서 top 10을 막대그래프로 그리기

def plot_gdp(rows):
    gdp = rows[:10, 1]
    indices = np.arange(10)

    plt.bar(indices, gdp, color='b')    # html 컬러표 찾아서 보기
    plt.xticks(indices , rows[:10, 0])

    plt.show()

plot_gdp(rows)

