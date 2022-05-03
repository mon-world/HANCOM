# 12_02_function.py

# 퀴즈
# 매개 변수 3개 함수 + 여러 방법 호출

def f_1(a, b, c):
    print(a, b, c)


f_1(1, 2, 'c')              # positional
f_1(a=1, b=2, c=3)          # keyword => end=''도 그거임

# f_1(a=1, 2, c=3)            # error. positional은 keyword 앞에만 가능

def f_2(a=0, b=0, c=0):
    print(a, b, c)


f_2()
f_2(1, 2)

# 퀴즈
# 가변인자를 매개변수로 받는 함수 + 호출
def f_3(*args):
    print(args)


f_3()
f_3(1, 2)

# PEP8 읽어보기