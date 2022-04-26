# 01_01_basic.py

print(1234)


# ctrl + shift + f10 : 윈도우 버전으로 메인실행을 지금 실행으로 바꿈

# 문제
# 화면에 13579를 5번 출력하세요

num = [str(i) for i in range(1, 10, 2)]

for i in range(5):
    print(''.join(num))

a = 3

# 문제
# 변수 a에 들어있는 값을 출력하세요

print(f'a={a}')

# 문제
# 변수 a에 값을 7로 바꾸세요

a = 7
print(f'a={a}')

b = 3

# 문제
# a와 b에 들어있는 값을 교환하세요

# c = b
# b = a
# a = c
#
# print(a, b)

a, b = b, a
print(f'a:{a}, b:{b}')

a1, b1 = 7, 3
