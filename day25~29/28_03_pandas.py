# primary key / PK FK
# df.pivot_table : 보고싶은것만 본다~

# 28_03_pandas.py
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)


def latest_basic():
    links = pd.read_csv('data/ml-latest-small/links.csv')       # movieId, imdbId, tmdbId
    movies = pd.read_csv('data/ml-latest-small/movies.csv')     # movieId, title, genres
    ratings = pd.read_csv('data/ml-latest-small/ratings.csv')   # userId, movieId, rating, timestamp
    tags = pd.read_csv('data/ml-latest-small/tags.csv')         # userId, movieId, tag, timestamp

    print(links.head(3), end='\n\n')        # [9742 rows x 3 columns]
    print(movies.head(3), end='\n\n')       # [9742 rows x 3 columns]
    print(ratings.head(3), end='\n\n')      # [100836 rows x 4 columns]
    print(tags.head(3), end='\n\n')         # [3683 rows x 4 columns]

    # 제주, 서귀포
    # 맑음
    # 흐림
    # ->
    # 제주, 서귀포 맑음
    # 제주, 서귀포 흐림


def older_basic():
    # [3883 rows x 3 columns]
    movies = pd.read_csv('data/ml-1m/movies.dat', sep='::', engine='python', header=None,
                         encoding='ISO-8859-1',
                         names='MovieID::Title::Genres'.split('::'))
    # print(movies)

    # [6040 rows x 5 columns]
    users = pd.read_csv('data/ml-1m/users.dat', sep='::', engine='python', header=None,
                        names=['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code'])
    # print(users)

    # [1000209 rows x 4 columns]
    ratings = pd.read_csv('data/ml-1m/ratings.dat', sep='::', engine='python', header=None,
                          names='UserID::MovieID::Rating::Timestamp'.split('::'))
    # print(ratings)

    # ratings: [UserID, MovieID, Rating, Timestamp]
    # ratings + users: [UserID, Gender, Age, Occupation, Zip-code, MovieID, Rating, Timestamp]
    # ratings + users + movies: [UserID, Gender, Age, Occupation, Zip-code, MovieID, Title, Genres, Rating, Timestamp]

    # [1000209 rows x 8 columns]
    df = pd.merge(users, ratings)           # UserID 기준
    # print(df)

    # [1000209 rows x 10 columns]
    df = pd.merge(df, movies)               # MovieID 기준
    # print(df)

    df.to_csv('data/ml-1m/binds.csv')


# latest_basic()
# older_basic()         # 3개로 나누어진 파일을 1개로 통합

# [1000209 rows x 10 columns]
df = pd.read_csv('data/ml-1m/binds.csv', index_col=0)
# print(df)

# UserID, Gender, Age, Occupation, Zip-code, MovieID, Rating, Timestamp, Title, Genres  # 컬럼의 이름
p1 = df.pivot_table(index='Gender', values='Rating')
# print(type(p1))       # <class 'pandas.core.frame.DataFrame'>
print(p1, end='\n\n')
#           Rating
# Gender
# F       3.620366
# M       3.568879

# 퀴즈
# 남녀 평균 평점을 구하세요
p2 = df.pivot_table(columns='Gender', values='Rating')
print(p2, end='\n\n')
# Gender         F         M
# Rating  3.620366  3.568879

# 퀴즈
# pivot_table 함수를 사용하지 말고, 직접 남녀 평점 평균을 구하세요
gender = df.values[:, 1]
print(gender[:10])          # ['F' 'M' 'M' 'M' 'M' 'F' 'M' 'F' 'F' 'M']

ratings = df.values[:, 6]
print(ratings[:10])         # [5 5 4 4 5 4 5 5 3 5]

# 1번
m, f = [], []
for g, v in zip(gender, ratings):
    # print(g, v)
    if g == 'M':
        m.append(v)
    else:
        f.append(v)

print('  male :', np.mean(m))       #   male : 3.5688785290984373
print('female :', np.mean(f))       # female : 3.6203660120110372
print()

# 2번
males = ratings[gender == 'M']
females = ratings[gender == 'F']
print('  males :', males.mean())
print('females :', females.mean())
print()

# 3번
print('  males :', df.Rating[df.Gender == 'M'].mean())
print('females :', df.Rating[df.Gender == 'F'].mean())
print()

print('  males :', df.Rating.values[df.Gender.values == 'M'].mean())
print('females :', df.Rating.values[df.Gender.values == 'F'].mean())
print()








# 퀴즈
# 직업별, 남녀 성별, 연령별 평점 구하기
p5 = df.pivot_table(index='Occupation', columns=['Age','Gender'], values='Rating')  # 멀티인덱스, 멀티콜럼스
print(p5, end='\n\n')
# NaN : 결측치 : 값 x : missing value
p6 = df.pivot_table(index='Occupation', columns=['Age','Gender'], values='Rating', fill_value=0)    # 0으로 바꾸기
print(p6, end='\n\n')

p7 = df.pivot_table(index='Occupation', columns=['Age','Gender'], values='Rating', aggfunc=[np.mean, np.sum])   # 평균, 섬 함수
print(p7, end='\n\n')

# 퀴즈
# 아래 결과를 구해서 p7과 동일하게 출력하세요
p8 = df.pivot_table(index='Occupation', columns=['Age','Gender'], values='Rating', aggfunc=[np.mean])
p9 = df.pivot_table(index='Occupation', columns=['Age','Gender'], values='Rating', aggfunc=[np.sum])

pd.concat([p8, p9], axis=0, end='\n\n')
pd.concat([p8, p9], axis=1, end='\n\n')