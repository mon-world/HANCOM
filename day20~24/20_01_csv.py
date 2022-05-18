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

rows = read_weather('data/weather.csv')
print(*rows, sep='\n')