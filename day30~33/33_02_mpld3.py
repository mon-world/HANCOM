# 33_02_mpld3.py

import mpld3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def sample_plot(df, title):
    df.plot(kind='line',
            marker='p',     # 펜타곤 = 5각형
            color=['red', 'blue'],
            lw=3,           # lind width
            ms=20,          # marker size
            alpha=0.7)      # 투명도 70퍼
    plt.title(title)
    plt.text(s='red line', x=1.7, y=2.5, color='red')
    plt.text(s='blue line', x=1.7, y=2.5, color='blue')


c1 = [1, 3, 2, 4]
c2 = [3, 4, 1, 2]

df = pd.DataFrame({'c1':c1, 'c2':c2})
sample_plot(df, 'base')

plt.show()
# plt.xkcd() 하면 보드마카로 그린 듯 된다.

# 내가 그린 그래프를 크롬에 그릴 수 있다.
# mpld3는 예쁜건 적고, 마우스 올리면 보여줌 - 크롬에서 열었을 때