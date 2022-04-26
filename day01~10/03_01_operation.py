# 퀴즈
# 아래 코드는 2개 변수의 값을 교환하는 코드입니다.
# 산술 연산자를 활용해서 임시 변수 c를 사용하지 않는 코드로 바꾸세요
# c = a
# a = b
# b = c
#
# a, b = 3, 7
#
# a = a + b   # a = 10, b = 7
# b = a - b   # a = 10, b = 3
# a = a - b   # a = 7 , b = 3
#
# print(f'a:{a}, b:{b}')  # a:7, b:3
#
# # 0 넣으면 곱셈, 나눗셈 안되니까 + - 사용해야함
#
# # 퀴즈
# # 산술 복합 연산자(+=)을 사용하는 코드로 수정하세요
#
# a += b
# b = a - b
# a -= b
#
# print(f'a:{a}, b:{b}')
#
# # print('rain' + str('777'))
#
# print(map(int(a, b)))


a = int(input())
b = int(input())
print(a + b)
