# 14_03_dict.py


a = {}
print(type(a))  # dict
print()

b = {1, 2, 3}
print(type(b))  # set
print()

d = {'name': 'kim', 'age': 25}
print(d)
print(type(d))
print()

d['hobby'] = 'netflix'      # insert

d['hobby'] = 'climbing'     # update
print(d)
print()

print(d.keys())
print(d.values())
print(d.items())
print()


# 퀴즈
# dict와 keys 함수를 반복문과 연동하세요
for k in d.keys():
    # print(k, d[k])        # k만 쓰면 틀림
    print('{:>5} : {:<10}'.format(k, d[k]))     # 왼 오 정렬
print()


# 퀴즈
# 딕셔너리의 items 함수를 반복문과 연동하세요
for kv in d.items():
    print(kv, kv[0], kv[1])         # 튜플 없애기 가능. 0은 키, 1은 벨류
print()

# 파이썬 스럽게 고치기
for k, v in d.items():
    print(k, v)
print()

# 퀴즈
# 딕셔너리의 items ㅎ마수를 반복문과 연동하고, 압쪽에 순서도 출력하세요
# 0 name kim
# 1 age 25
# 2 hobby climbing
i = 0
for k, v in d.items():
    print(i, k, v)
    i+=1
print()

# 파이썬 스럽게 고치기
for i, kv in enumerate(d.items(),1 ):    # 데이터는 2개. 숫자와 튜플. 순서 필요할 떄 쓴다.
    # 2번째 매개변수 사용시 그것부터 센다.
    print(i, kv)
print()

# 데이터는 2개인데 3개로 나눠서 에러남
# for i, k, v in enumerate(d.items()):    
#     print(i, k, v)

# 3개 같은 2개라는 뜻
for i, (k, v) in enumerate(d.items()):    
    print(i, k, v)
print()

# 가장 편함: 키 호출 필요x
for k in d:
    print(k, d[k])