# 16_01_loop.py

import random
import string

# 퀴즈
# 랜덤 알파벳(대문자, 소문자)으로 구성된 길이 20인 문자열을 반환하는 함수를 만드세요
def make_alphabets(size):
    text = ''

    alpha = string.ascii_letters + ' '
    for _ in range(size):
        # n = random.randrange(len(alpha))
        # text += alpha[n]
        text += random.choice(alpha)

    return text

# 퀴즈
# make_alphabets 함수가 반환된 문자열에서
# 소문자 갯수와 대문자 갯수를 반환하는 함수를 만드세요
def count_lower_and_upper(chars):
    lower, upper = 0, 0
    # 여러개를 가지고 있으면 반복할 수 있으므로
    # for c in chars:
    #     # 문자 하나씩 분할 : 대 소문자 구분
    #     # print(c, ord(c))
    #     idx = ord(c)
    #     if 65 <= idx <= 90:
    #         upper += 1
    #     elif 97 <= idx <= 122:
    #         lower += 1

    # ord를 쓰지 않고 더 쉽게
    for c in chars:
        if 'A' <= c <= 'Z':
            upper += 1
        elif 'a' <= c <= 'z':
            lower += 1

    return lower, upper

def count_lower_and_upper1(chars):
    lower, upper = 0, 0

    # 1번
    # for c in chars:
    #     # print(c, ord(c))
    #     idx = ord(c)
    #
    #     if 65 <= idx <= 90:
    #         upper += 1
    #     elif 97 <= idx <= 122:
    #         lower += 1

    # 2번
    # for c in chars:
    #     if 'A' <= c <= 'Z':
    #         upper += 1
    #     elif 'a' <= c <= 'z':
    #         lower += 1

    # 3번
    # for c in chars:
    #     if 'A' <= c <= 'Z':
    #         upper += 1
    #     else:
    #         upper += 0
    #
    #     if 'a' <= c <= 'z':
    #         lower += 1
    #     else:
    #         lower += 0

    # 4번
    for c in chars:
        upper += ('A' <= c <= 'Z')
        lower += ('a' <= c <= 'z')

        # if 'A' <= c <= 'Z':
        #     upper += ('A' <= c <= 'Z')
        # else:
        #     upper += ('A' <= c <= 'Z')

        # if 'a' <= c <= 'z':
        #     lower += ('a' <= c <= 'z')
        # else:
        #     lower += ('a' <= c <= 'z')

    return lower, uppe


random.seed(17)
chars = make_alphabets(20)
print('[{}]'.format(chars))

print(count_lower_and_upper(chars))