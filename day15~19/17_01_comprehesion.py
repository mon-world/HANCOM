# 17_01_comprehesion.py

import random

# 컴프리헨션 - 한 줄 짜리 반복문

s = 0
for i in range(5):
    s+=i
print(s)

print([i for i in range(5)])
print(sum([i for i in range(5)]))
print(len([i for i in range(5)]))


# 퀴즈
# 100 보다 작은 난수 10개로 이루어진 리스트 반환 함수

def out_10():
    list_a = []
    for _ in range(10):
        list_a.append(random.randrange(-100, 100))
    return list_a

print(out_10())

# 퀴즈
# 100보다 작은 양수 10개로 구성된 리스트를 만드세요

list_10 = [random.randrange(100) for _ in range(10)]
print(list_10)

# 퀴즈
# 난수 리스트에서 홀수만으로 구성된 리스트를 만드세요

a = [random.randrange(100) for _ in range(10)]
b = [i for i in a if i % 2] # a에 대한 거니까 뒤에
print(b)

# 퀴즈
# 문자열 리스트에 들어있는 모든 단어의 길이 합계를 구하세요
words = ['holiday', 'clean', 'food']

# 연습
s = 0
for i in words:
    s += len(i)
print(s)

# 컴프리헨션
print(sum([len(i) for i in words]))

# 퀴즈
# 여러 개의 1차원 리스트에서 가장 큰 값을 찾으세요
c1 = [random.randrange(100) for _ in range(10)]
c2 = [random.randrange(100) for _ in range(10)]
c3 = [random.randrange(100) for _ in range(10)]

# 아주 쉽게 생각하자
print(max(c1 + c2 + c3))

# 퀴즈
# 2차원 리스트를 1차원 리스트로 변환하세요
c = [c1, c2, c3]
s = []
for i in c:
    for j in i:
        s.append(j)

print(s)

s1 = [j for i in c for j in i]
print(s1)











