# 28_03_pandas.py
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

movies = pd.read_csv('data/movie_lens/ml-latest-small/movies.csv')
links = pd.read_csv('data/movie_lens/ml-latest-small/links.csv')
ratings = pd.read_csv('data/movie_lens/ml-latest-small/ratings.csv')
tags = pd.read_csv('data/movie_lens/ml-latest-small/tags.csv')
print(movies.head(3), end='\n\n')
print(links.head(3), end='\n\n')
print(ratings.head(3), end='\n\n')
print(tags.head(3), end='\n\n')

# primary key / PK FK
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
    # concat 사용 불가 : shape가 다름 + 중복제거
    # df.merge 사용 : 고유값(key) 기준으로 병합

    # [1000209 rows x 8 columns]
    df = pd.merge([users, ratings])
    # print(df)

    # [1000209 rows x 10 columns]
    df = pd.merge(df, movies)
    print(df)

older_basic()

# df.pivot_table : 보고싶은것만 본다~