# 18_01_comprehension.py

# 퀴즈
# 10000보다 작은 양수에 들어있는 8의 갯수를 구하시오
# 808 -> 2

# n = int(input())
# s = []
# for i in str(n):
#     s.append(int(i))
#
# print(s)

# print(len([i for i in str(n) if str(i) == '8']))

# len([i for i in str(n) if str(i) == '8']) : 1개 입력받으면 나옴

s1 = 0
for j in range(10000):
    s2 = len([i for i in str(j) if str(i) == '8'])
    s1 += s2

# len 안쓰려면? 그냥 세기

s2 = 0
for j in range(10000):
    for c in str(j):
        if c == '8': # 쪼개져서 반복된다.
            s2 += 1

print(s1)
print(s2)

print()

# for _ in range(10000) len([i for i in str(j) if str(i) == '8']) ???

print(len([i for j in range(10000) for i in str(j) if i == '8']))

# 훨씬 깔끔하게
def count_8(n):
    cnt = 0
    for c in str(n):
        cnt += (c == '8')
    return cnt

print()
print([count_8(n) for n in range(10000)])
print(sum([count_8(n) for n in range(10000)]))

# 정식 코드
print(sum([str(n).count('8') for n in range(10000)]))

# 출력은 같음
print(type(list(range(10))))
print(type(str(list(range(10)))))