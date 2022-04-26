# 07_01_function.py

# 퀴즈
# 더하기 만들기
# 다른거 사용하는게 좋긴해 변수

def sum(a, b):
    return print(a + b)


a = 71
b = 31


# 퀴즈
# 두 개의 정수 중에서 큰 숫자를 찾는 함수를 만드세요

def max_2(a, b):
    # if a > b:
    #     return a
    # else:
    #     return b

    # if a > b:
    #     return a
    #
    # return b    # 같은코드임

    # return 1개 쓰기
    # if a > b:
    #     x = a
    # else:
    #     x = b
    # return x

    # 더 간단히
    if a > b:
        b = a
    return b

    # 더더 간단히
    # return a if a > b else b  # 한줄로 사용하는 if문
print(max_2(a, b))

# 리턴이 아니라 print로 하면 변수저장을 못한다. c = compare(7, 3) 불가능함.
# 이렇게 저장하면 None값이 나온다.
# return 뒤에 오는거는 출력 안되넹.

print('-'*30)

# 퀴즈
# 4개의 정수 중에서 가장 큰 숫자를 찾는 함수를 만드세요

def max_4(a, b, c, d):
    return max_2(a,max_2(b,max_2(c,d)))

print(max_4(1,2,3,4))

# 웨않되???
def max4(a, b, c, d):
    # if a == b == c == d:
    #     return a
    #
    if a == b:
        if c == d:
            if b == c:
                return a
            else:   # 3 3 2 2
                max4(a, c, a, c)
        else:
            max4(c, d, a, a)

    elif a > b:
        max4(a, a, c, d)
    else:
        max4(b, b, c, d)


print(max4(1,2,3,4))









