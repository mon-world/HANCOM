# 23_01_sort.py

ns = [4 ,6, 7, 1, 23, 53543]

print(sorted(ns))

print(ns)

ns.sort()           # 스스로 나 자신을 바꿈.

print(ns)

# key라는 매개변수 : 함수를 만들어서 전달한다.

def last_digit(n):
    print(n)
    return n % 10

ns.sort(key=last_digit)         # callback. 잘 사용 안함
print(ns)

# 퀴즈
# 문자열 리스트를 정렬하세요
colors = ['YELLOW', 'BLUE', 'RED', 'WHITE']

print(sorted(colors))



def to_upper(s):
    return s.upper()        # 하나하나 매개변수로 넘어오는데 어퍼는 뭐지

# 람다식 표현. 반환값을 갖는 한줄짜리 함수
# 콜론의 왼쪽 매개변수, 오른쪽은 함수
colors.sort(key=lambda s: s.upper())

colors = ['YELLOW', 'blue', 'Red', 'whItE']
print(colors)

colors.sort(key=to_upper)
print(colors)


# 퀴즈
# 문자열 리스트를 길이순으로 내림차순 정렬
def len_list(s):
    return len(s)
colors.sort(key=len_list, reverse=True)
print(colors)















