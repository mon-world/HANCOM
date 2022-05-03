# 12_01_for.py

for _ in range(5):
    print('*'*5)
print()

# 퀴즈
# 아래와 같은 모양으로 출력하는 함수를 작성하세요(triangle_1)
# 2차ㅜ언
# *
# **
# ***
# ****

def triangle_1(numbers):
    for i in range(1, numbers + 1):
        for _ in range(i):
            print('*', end='')
        print()

triangle_1(5)

# 퀴즈
# 위 모양을 뒤집은 모양을 출력하는 함수를 만들기

def triangle_2(numbers):
    for i in range(numbers, 0, -1):
        for _ in range(i):
            print('*', end='')
        print()

triangle_2(5)

# 퀴즈
# 공백 포함

def triangle_3(numbers):
    for i in range(numbers-1, -1, -1):
        for j in range(numbers-1, -1, -1):
            if i >= j:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()

    for i in reversed(range(numbers)):  # 중요!
        for j in reversed(range(numbers)):
            if i >= j:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()

triangle_3(5)