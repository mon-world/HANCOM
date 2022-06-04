# 34_01_stock.py

# 줄 바꿈 : 오른쪽 끝에 공백 2칸
# A : Above  
# B : Below  
# M : Markdown  
# ctrl + enter : Run

import FinanceDataReader as fdr
import pandas as pd
import time
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)


def stock_basic_1():
    # 주식거래소에 상장된 모든 종목 가져오기
    # 코스피, 코스닥, 코넥스
    stock_1 = fdr.StockListing('KRX')
    print(stock_1)

    stock_2 = stock_1.loc[stock_1['Market'] != 'KONEX']
    print(stock_2)

    stock_3 = stock_2.loc[stock_2['Region'].notnull()]
    print(stock_3)

    stock_3.to_csv('data/stock_company.csv', sep='\t')


def stock_basic_2():
    df = pd.read_csv('data/stock_company.csv', sep='\t', index_col=0)
    print(df)


# 퀴즈
# 삼성전자 작년 주가를 가져와서 그래프로 그려보세요 (종가 기준)
def stock_basic_3():
    data = fdr.DataReader(symbol='005930', start='2021.12.1', end='2021.12.31')
    print(data)

    dates = data.index.values
    dates = [str(d) for d in dates]
    dates = [d[:10] for d in dates]
    print(dates)

    y = data.Close.values
    x = range(len(y))

    plt.plot(x, y)
    plt.xticks(x, dates, rotation=45)
    plt.title('Samsung Stock Price')
    plt.show()


# stock_basic_1()
# stock_basic_2()
stock_basic_3()










