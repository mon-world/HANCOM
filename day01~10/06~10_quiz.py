# 2주차 퀴즈 풀이

# --------------------------------------------- #

a = 3
b = 7
c = 1

# 양의 실수 a에 들어있는 값 중에서 정수 부분만 추출하세요 (3가지)
# 1. int 형으로 변환
print(int(a))

# 2. 몫 연산하기
print(a//1)

# 3. 소숫점 빼기
print(a - a%1)

# 양의 정수 b가 3의 배수이거나 5의 배수인지 알려주세요
print(b % 3 == 0 or b % 5 == 0)

# 정수 c가 음수인지 0인지 양수인지 알려주세요 (elif 사용 금지)
if c:
    if c>0 : print('양수')
    else   : print('음수')
else: print('0')

print('-'*30)
print('-'*30)
print('-'*30)

# --------------------------------------------- #

# 두 개의 정수를 더한 결과를 반환하는 함수를 만드세요
def sum_2(a, b):
    return a + b

print(sum_2(a, b))
print('-'*30)

# 두 개의 정수 중에서 큰 숫자를 찾는 함수를 만드세요 (3가지)
def comp(a, b):
    return a if a > b else b

print(comp(a, b))
print('-'*30)

# 4개의 정수 중에서 가장 큰 숫자를 찾는 함수를 만드세요 (3가지)
def comp_4(a, b, c, d):
    return comp(a, comp(b, comp(c, d)))

print(comp_4(5 ,6, 7, 11))
print('-'*30)

# --------------------------------------------- #

# 0부터 4까지 출력하는 반복문을 만드세요
# (range 함수 3가지 버전 사용)
for i in range(5):
    print(i, end=' ')
print()
print('-'*30)

# 0에서부터 24까지의 숫자를 출력하는 함수를 만드세요 (반복문 1개)
# 한 줄에 5개씩 출력합니다
for i in range(25):
    print(i, end=' ')
    if i % 5 == 4 : print()
print('-'*30)

# 0에서부터 24까지의 숫자를 출력하는 함수를 만드세요 (반복문 2개)
# 한 줄에 5개씩 출력합니다
def print_0_24():
    for i in range(5):
        for j in range(5):
            print(5*i + j, end=' ')
        print()
    print()

print_0_24()
print('-'*30)

# --------------------------------------------- #

# 점수를 학점으로 변환하는 함수를 만드세요
#  0 ~  60   F
# 61 ~  70   D
# 71 ~  80   C
# 81 ~  90   B
# 91 ~ 100   A

# 앞에서 만든 코드에 대해 입력 범위가 정해져 있지 않을 때의 코드로 수정하세요

# 정수를 입력 받는 input 함수를 5회 호출해서 최대값을 구하세요

# 정수를 입력 받는 input 함수를 여러 번 호출해서 최대값을 구하는 함수를 만드세요 (input 1회 이상)

# --------------------------------------------- #

# 리스트를 거꾸로 출력하세요
a = [1, 2, 3, 4, 5]

def reverse_list(num):
    x = []
    for i in num:
        x.insert(0, i)
    return x

print(reverse_list(a))
print('-'*30)
# --------------------------------------------- #

# 100보다 작은 난수 10개로 이루어진 리스트 반환하는 함수를 만드세요
import random

def out_10(num):
    x = []
    for i in range(num):
        x.append(random.randrange(100))
    return x

rand_list = out_10(10)
print(rand_list)
print('-'*30)

# 리스트에 가장 큰 숫자를 찾는 함수를 만드세요

def find_big(num):
    x = num[0]
    for i in num:
        if x < i : x = i
    return x

print(find_big(rand_list))
print('-'*30)

# 리스트에 포함된 홀수 중에서 가장 큰 숫자를 찾는 함수를 만드세요 (최소 1개는 홀수)

def find_odd_big(num):
    x = []
    for i in num:
        if i % 2: x.append(i)
    return find_big(x)

print(find_big(rand_list))

# 리스트를 거꾸로 뒤집는 함수를 만드세요
# 리스트 거꾸로 출력과 동일

