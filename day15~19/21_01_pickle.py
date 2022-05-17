# 21_01_pickle.py

import csv_module
import pickle


# 피클은 파이썬 객체 입출력에 사용한다.


def save_by_pickle(rows, file_path):
    # 1. 파일 오픈하기
    f = open(file_path, 'wb')
    # binary 형태로 저장하므로 w가 아닌 wb
    # 바이너리는 텍스트가 아니므로 인코딩을 쓰지 않는다.

    # 2. 피클로 저장 - 루프 돌 필요 없음
    pickle.dump(rows, f)
    f.close()

# rows = csv_module.read_csv('data/weather.csv')
# save_by_pickle(rows, 'data/weather.csv')

# 퀴즈
# csv_module 파일에 만든 함수를 아무거나 불러와서 결과를 출력하기

# rows = csv_module.read_csv('data/weather.csv')
# print(*rows)


# 퀴즈
# 피클로 저장한 데이터를 반환하는 함수 만들기

def load_by_pickle(file_path):

    # f = open(file_path, 'rb')
    # rows = pickle.load(f)
    # f.close()

    # with를 사용하는 목적 : close() 안써도 됨
    with open(file_path, 'rb') as f:
        return pickle.load(f)


rows = load_by_pickle('data/weather.csv')
print(*rows, sep='\n')

