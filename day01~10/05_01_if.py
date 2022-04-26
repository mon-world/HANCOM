# 05_01_if.py


# 0보다 큰 양의 정수가 있는데
# 이 값은 홀 or 짝 ?

# n = int(input())
# if n % 2 == 0:
#     print("짝수")
# else :
#     print("홀수")

a = -1

# print(a%2 == 0 )

# 1은 참 대표임. 0이 아닌 모든 숫자는 bool(a) = True, bool(0) = False
# if 뒤는 모두 참, 거짓으로 해석한다.
# if a % 2:  # a%2로만 써도 된다. 1은 참 0은 거짓.
#     print('홀수')
# else:
#     print('짝수')


# 퀴즈 : 무조건 짝수
if a:
    print('짝수')
else:
    print('짝수')

# 퀴즈
# 양의 정수를 입력 받아서 자신보다 큰 첫 번째 짝수를 출력하세요

# n = int(input())
#
# print(n + 2 - (n % 2))


# if n % 2:
#     print(n+1)
# else:
#     print(n+2)

# print를 줄이는 경우가 좋음.
# b = 0
# if b % 2:
#     b += 1
# else:
#     b += 1
# print(b)

c = '7'  # input('양수 : ')
c = int(c)

# 1번
if c % 2:
    print(c + 2 - 1)
else:
    print(c + 2 - 0)

# 2번
if c % 2:
    print(c + 2 - c % 2)
else:
    print(c + 2 - c % 2)

# 3번
print(c + 2 - c % 2)

print('-'*30)

# 문제
# 양의 정수가 항상 짝수가 되게 만드세요
x = 3
print(x -(x % 2))

if x % 2:
    x -= 1
print(x)