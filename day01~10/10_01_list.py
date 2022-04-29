# 10_01_list.py

import random


print(random.randrange(90, 100, 3))

# 퀴즈
# 100 보다 작은 난수 10개로 이루어진 리스트 반환 함수

def out_10():
    list_a = []
    for _ in range(10):
        list_a.append(random.randrange(-100, 100))
    return list_a

print(out_10())

# 힘들다
def randoms_10():
    a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    for i in range(10):
        # print(random.randrange(100), end=' ')
        a[i] = random.randrange(100)

    # print(a)
    return a


a = out_10()
print(a)





# 퀴즈
# 리스트에 포함된 홀수 중에서 가장 큰 숫자를 찾는 함수르 만드세요

def odd_big(numbers):
    # 홀수만 들어있는 리스트 만들기
    list_odd = []
    # for i in range(len(list)):
    #     if list[i] % 2 :
    #         list_odd.append(list[i])
    for i in range(len(numbers)) and numbers[i] % 2 : # and를 쓰면 짧아진다.
        list_odd.append(numbers[i])

    # max값 찾기
    odd = list_odd[0]
    for i in range(1, len(list_odd)):
        if odd < list_odd[i]:   # 코드 안뒤집어 지는게 낫다
            odd = list_odd[i]

    return odd

print(odd_big(a))

def odd_big_list(list):
    for i in range(len(list)):
        if list[i] % 2:
            odd = list[i]
            num = i
            break
    for i in range(num, len(list)):
        if list[i] % 2:
            if list[i] > odd: odd = list[i]

    return odd

print(odd_big_list(a))































