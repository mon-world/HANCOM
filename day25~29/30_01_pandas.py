# 30_01_pandas.py
import pandas as pd
import numpy as np

# df.Title == name : 왼쪽 시리즈. 데이터가 여러개 있다는것
# 왼쪽 : 스칼라. 배열과 스칼라가 만나느 것임. 즉, 값(스칼라)를 배열 전체에 전파
# 브로드캐스트.

df = pd.read_csv('data/ml-1m/binds.csv', index_col=0)
# print(df)

# 퀴즈
# 영화 제목별 남녀 성별 평점을 구하세요
by_gender = df.pivot_table(index='Title', columns='Gender', values='Rating')
print(by_gender, end='\n\n')

# 퀴즈
# 영화 평점 갯수가 500개 이상인 영화 제목을 구하세요
freq_1 = {}
for name in df.Title:
    if name not in freq_1:
        freq_1[name] = 0

    freq_1[name] += 1

print(*sorted(freq_1.items(), key=lambda t: t[1], reverse=True)[:10], sep='\n')
print()

for name in by_gender.index.values[:10]:
    print('{:>35} : {}'.format(name, np.sum(df.Title == name)))
print()

freq_2 = df.groupby(by='Title') # 타이틀로 그룹바이. 반복할시에는 객체의 형태로 나옴
freq_2 = df.groupby(by='Title').size()

index_500 = freq_2[freq_2 >= 500]

# 퀴즈
# by_gender 로부터 index_500에 포함된 영화에 대한 평점 구하기
title_500 = index_500.index.values

# print(by_gender.iloc[0])
# print(by_gender.loc['10 Things I Hate About You (1999)'])
# 
# for name in title_500:
#     print(by_gender.loc[name])

rating_500 = by_gender.loc[title_500]
print(rating_500, end='\n\n')

# 퀴즈
# 여자가 좋아하는 영화 top5 구하기
f_top = pd.DataFrame.sort_values(rating_500, by='F', ascending=False)
print(f_top, end='\n\n')

# 퀴즈
# 여성들이 남성들보다 평점 잘 준 영화 top5 구하기
# by_gender : 남 여 데이터 빼면 됨
rating_500['Diff'] = by_gender['F'] - by_gender['M']

# 그냥 [], iloc, loc 차이는???















