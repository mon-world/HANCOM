# 13_03_file.py

def show_strip():
    text ='\n\n\n\t\t\t\t   this weekend    \t\t\t\n\n\n'
    print(text)
    print(text.strip())             # 문자열의 양쪽 공백을 모두 제거한다.
    print('[{}]'.format(text.strip()))  # 포멧 중요


def read_file_2():
    f = open('data/poem.txt', 'r', encoding='utf-8')
    
    while True:
        line = f.readline()
        # print(len(line))
        
        # if len(line) == 0: 파이썬에선 좋은 표현 아님.
        # if not len(line):
        if not line:            # 한글자라도 있다면 계속하기. 문자열도 참 거짓 판단 가능
            break
        
        print(line, end='')

    f.close()

def read_file_3():
    f = open('data/poem.txt', 'r', encoding='utf-8')

    for line in f:
        print(line.strip())         # 문자열 양쪽 끝 공백 모두 삭제

    f.close()

# 퀴즈
# 파일을 읽어서 반환하는 함수를 만드세요(내용 전체)
def read_file_Q1(files):
    f = open(files, 'r', encoding='utf-8')

    text = ''
    for line in f:
        # print(line.strip())
        text += line            # 단락을 보존하기 위헤 strip을 안함.

    f.close()
    return text

def read_file_4():
    # with 옆은 변수 사용 x. as로써 별명 만들어줌
    # 장점 : close 호출 안해도 된다.
    with open('data/poem.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())         # 문자열 양쪽 끝 공백 모두 삭제

# 쌍을 이루는 것들을 반드시 먼저 코딩하라.

# 퀴즈
# 파일을 읽어서 반환하는 함수를 만드세요(내용 전체 포함된 문자열 리스트)
def read_file_Q2():
    x = []
    with open('data/poem.txt', 'r', encoding='utf-8') as f:
        for line in f:
            x.append(line.strip())

    return x

def read_file_Q22():
    with open('data/poem.txt', 'r', encoding='utf-8') as f:
        return list(f)      # 개행문자 있긴 함

read_file_Q2()

# join : 문자열 리스트를 하나의 문자열로 합친다.
row = read_file_Q22()
print('\n'.join(row))   # 문자마다 개행문자 들어감 사이사이