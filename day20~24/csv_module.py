# 20_01_csv.py
import csv


# 퀴즈
# csv 파일을 읽어서 반환하는 함수 만들기
# 2차원 리스트 반환

def read_weather(file):
    x = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:  # 가장 편함
            x.append(line.strip().split(','))
            # strip의 사용 이유는?
        # x = [line.strip().split(',') for line in f]
        # x = [line for ine in csv.reader(f)]
        # 실제로는 csv 모듈 사용하는게 좋다. 중간에 , 사용할수도 있음
        # us-500.csv

    f.close()
    return x

def read_csv(file_path):
    f = open(file_path, 'r', encoding='utf-8')

    rows = [line for line in csv.reader(f)]
    f.close()

    return rows



print(__name__) # 충돌 안나게?
# __name__은 다음 조건에 다음과 같은 값을 같는다.
# csv_module : 다른 곳에 import 되었을 때
# __main__ : import 되지 않았을 때

if __name__ == '__main__':
    # rows = read_weather('data/weather.csv')
    rows = read_csv('data/weather.csv')
    print(*rows, sep='\n')