# 21_02_sqlite.py

import csv_module
import sqlite3          # sql : structured(string) query language

'''
브라우저에 sqlite3 사용법 검색
재실행시 에러 : 테이블이 만들어져 있는데 또 만드는 것이므로

db는 용량을 줄이기 위해 table을 만든다.
1 서울 12 제주도 이렇게 / 숫자는 pk : primary key(유일)
1 서울 2 서울 가능 / 1 서울 1 대구 불가능
사용자에게 줄 때만 흩어진 데이터를 합쳐줌 => join

프라이머리 키를 지정하지 않고 넣으면, 일련번호가 만들어져서 모두 유니크
따라서 3번 실행하면 3천

data table에 있는 12..?
foreign key...? => 외래키.

csv는 db사용 못할 때 써라. db가 더 낫다.
'''

# CRUD : Create, Read, Update, Delete
# def create_table(db_path):
#
#     # 원격이면 id pw ip등이 들어간다.
#     # 파이썬으로 오라클 등 좋은 db 서버에 접근하고 싶다면, 해당 모듈 사용
#
#     # 서버 연결
#     conn = sqlite3.connect(db_path)
#     # 커서를 만든다 : 데이터가 있는 위치를 알려준다 라고 생각
#     cur = conn.cursor()
#
#     query = 'CREATE TABLE db_list (id INTEGER, name VARCHAR(16))'    # 대 소문자 구분 x
#     # (컬럼의 이름, 컬럼의 데이터 타입)
#     # db는 데이터가 많으므로 세분화시켜서 dtype이 더 많다.
#     cur.execute(query)
#
#     # 한번에 모아서 반응하는 시스템
#     conn.commit()
#     # db 끔
#     conn.close()

def create_table(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    query = 'CREATE TABLE kma (prov TEXT, city TEXT, mode TEXT, tmEf TEXT, wf TEXT, tmn TEXT, tmx TEXT, rnSt TEXT)'
    cur.execute(query)

    conn.commit()
    conn.close()


# data를 1개 집어넣는 코드
def insert_row(db_path, rows):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 데이터 갯수를 알려주기 위해? 쓰기 위해 포멧 사용
    # 큰 따옴표가 있어야함 => 문자로 인식하게 하기 위해 "{}" : sqlite 규칙
    # 숫자와 문자열의 구별을 위해 문자는 ""로 해준다.

    # 1번
    # values = 'VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    # 2번
    # values = 'VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(*row)
    # query = 'INSERT INTO kma (prov, city, mode, tmEf, wf, tmn, tmx, rnSt) ' + values

    # 3번
    prov, city, mode, tmEf, wf, tmn, tmx, rnSt = row
    base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    query = base.format(prov, city, mode, tmEf, wf, tmn, tmx, rnSt)
    cur.execute(query)

    conn.commit()
    conn.close()

    # 문제점
    # 1. 데이터 넣는 데에 시간이 오래 걸린다 : commit을 너무 많이 한다.
    # 1개 집어넣고 커밋하고 닫음. 이게 가장 오래걸림.
    # 커밋은 여러개 하고 난 후에 마지막에 바꿈.



def fetch_all(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    query = 'SELECT * FROM kma'         # * : all -> 데이터 집어넣고 모두 읽어온다? 위험

    # 아래 코드 줄이기
    # rows = []
    # for row in cur.execute(query):      # 반복문에 적용해야함
    #     print(row)

    # rows = [row for row in cur.execute(query)]
    
    # 더 간단히. 이유?? 어차피 같음
    rows = list(cur.execute(query))
    
    # conn.commit()         # 내부에 변화 있을 때만 호출이므로 여기선 필요 없음
    conn.close()

    return rows



db_path = 'data/weather.sqlite'
rows = csv_module.read_csv('data/weather.csv')
# create_table(db_path)

# 퀴즈
# weather.csv 파일로부터 가져온 데이터를 하나씩 db에 추가하는 함수를 만들기
# for row in rows:
#     insert_row(db_path, row)

# rows = fetch_all(db_path)
# print(*rows, sep='\n')

# 퀴즈
# weather.csv 파일로부터 가져온 데이터를 하나씩 db에 추가하는 함수를 만들기 : 커밋 1개

def insert_all(db_path, rows):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    for row in rows:
        prov, city, mode, tmEf, wf, tmn, tmx, rnSt = row
        # base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")' # 밖으로 뻄 반복 필요 x
        query = base.format(prov, city, mode, tmEf, wf, tmn, tmx, rnSt)
        cur.execute(query)

    conn.commit()
    conn.close()

# insert_all(db_path, rows)



# 퀴즈
# db로부터 원하는 특정 도시의 데이터만 반환하는 함수를 만들기

def fetch(db_path, city):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    query = 'SELECT * FROM kma WHERE tmEf="{}"'.format(city)
    rows = list(cur.execute(query))


    conn.close()

    return rows

# ???
rows = fetch(db_path, "2022-05-22 00:00")
print(rows)

































