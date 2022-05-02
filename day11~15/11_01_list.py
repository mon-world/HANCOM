# 11_01_list.py

import random

# 퀴즈
# 최대 5자리 양수에서 가장 큰 자릿수를 찾는 함수를 만드세요
# 65249 -> 9

a = random.randrange(100000)

def find_max(numbers):
    max_n = numbers[0]
    for i in numbers:
        if max_n < i:
            max_n = i

    return max_n


def fine_big_num(num):
    x = []
    for i in range(5):
        x.append(num % 10)
        num //= 10 # num = num // 10
    a = find_max(x)
    return a

print(fine_big_num(a))

# 간단히 합치기

def find_max_digit(num):
    n_max = num % 10 # 초기값
    for i in range(4): # 초기값을 설정해줬기 때문에 -1
        num //= 10

        if n_max < num % 10:
            n_num = num % 10

    return n_max

# 
def find_big_digit_by_str(num):
    s = str(num)
    c_max = s[0]
    for c in s:
        # print(c, end=' ')

        if c_max < c:
            c_max = c

    return c_max


# random.seed(21)
a = random.randrange(100000)
print(find_big_digit_by_str(a))

