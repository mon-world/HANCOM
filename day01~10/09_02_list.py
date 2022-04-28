#

a = [1, 3, 5]
print(len(a))

for i in range(len(a)):
    print(i, a[i])

print()
print('-'*30)
# 퀴즈
# 리스트를 거꾸로 출력하세요

for i in range(len(a)-1, -1, -1):
    print(a[i])     # 항상 이 곳이 간단한게 낫다.