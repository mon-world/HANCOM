# 08_01_for.py

# [) -> 왼쪽 포함 오른쪽 미포함
# 시작 끝 간격
# 0 1 2 3 4 = 0 5 1 = 0 4+1 1
# 4 3 2 1 0 = 4 -1 -1

# 0~100미만 짝수만 출력
# for문 안 쪽의 코드가 가장 가볍게 하는 것이 좋다.
# for i in range(1, 50, 1):   # 시작 종료 증감
#     print(2*i)
#
# for i in range(1, 100, 1):
#     print(i, end=' ')

print('\n')
print('-'*30)

# 퀴즈
# 0부터 24까지의 숫자를 출력하는 함수를 만드세요
# 한 줄에 5개씩 출력합니다

def print_5():
    for i in range(0,5,1):
        for j in range(0,5,1):
            print(5*i + j, end=' ')
        print('\n')

# print_5()

def pr_5():
    for i in range(25):
        if i % 5 == 0:
            print(end='\n')
        print(i, end=' ')

# pr_5()


# 퀴즈
# 반복문 안쪽의 코드에 대해 반복문으로 수정하기

print('ddddd')
for i in range(0, 25, 5):
    print(i+0, i+1, i+2, i+3, i+4)

print('\n')
print('-'*30)

for i in range(0, 25, 5):
    for j in range(5):
        print(i+j, end=' ')
    print()

print()
print('-'*30)

# 퀴즈
# 반복문 2개 사용한 코드에서 안쪽 반복문을 함수로 대체하기
for i in range(0, 25, 5):
    for j in range(5):
        print(i + j, end=' ')
    print()
print()

def inner(base):    # 매개변수
    for j in range(5):
        print(base + j, end=' ')
    print()

print('---')

for i in range(0, 25, 5):
    inner(i)
print()








