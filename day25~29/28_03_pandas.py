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