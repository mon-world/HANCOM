# 10_02_list.py

a = [2, 3, 5, 9, 11]
print(a)

# 불편
for i in range(len(a)):
    print(a[i], end=' ')
print()

# 편-안
for i in a:  # i는 반복변수에 주로 사용한다.
    print(i, end=' ')
print()


# 퀴즈
# 수정하기
def find_max(numbers):
    max_n = numbers[0]
    for i in numbers:
        if max_n < i:
            max_n = i

    # print(max_n)
    return max_n


# 리스트에 포함된 홀수 중에서 가장 큰 숫자를 찾는 함수를 만드세요 (최소 1개는 홀수)
def find_max_among_odd(numbers):
    odds = []
    for i in numbers:
        if i % 2:
            odds.append(i)

    odd = odds[0]
    for i in odds:
        if odd < i:
            odd = i

    return odd


# 퀴즈
# 리스트를 거꾸로 뒤집는 함수를 만드세요

def reverse(num):
    rev = []
    for i in range(len(num) -1, -1, -1):
        rev.append(num[i])

    return rev

print(reverse(a))

# 리스트 추가 없이
def reverse_1(num):
    num = [num[x] for x in range(len(num)-1, -1, -1)]

    return num

print(reverse_1(a))