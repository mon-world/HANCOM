#

# 퀴즈
# 점수 학점 변환

def point2grade(point):
    if 91 <= point <= 100:
        grade = 'A'
    elif 81 <= point <= 90:
        grade = 'B'
    elif 71 <= point <= 80:
        grade = 'C'
    elif 61 <= point <= 70:
        grade = 'D'
    else:
        grade = 'F'

    return grade
    # elif로 해서 범위 줄일 수 있음.


print(point2grade(95))


# 더 간단히
def point2grade2(point):
    if point <= 60:
        grade = "F"
    elif point <= 70:
        grade = "D"
    elif point <= 80:
        grade = "C"
    elif point <= 90:
        grade = "B"
    else:
        grade = "A"
    return grade

print(point2grade2(95))

# 더 보기 좋게
# 초기값을 A로 두면 else 삭제 가능
def point2grade3(point):
    grade = 'A'
    if   point <= 60: grade = "F"
    elif point <= 70: grade = "D"
    elif point <= 80: grade = "C"
    elif point <= 90: grade = "B"

    return grade

# 퀴즈
# 앞에서 만든 코드에 대해 입력 범위가 정해져 있지 않을 때로 수정하시오.

def point2grade_1(point):
    grade = 'error'
    if 0 <= point <= 100: grade = point2grade(point)

    return grade

print()
print('-'*30)

# crtl shift f : 파일 안에 함수 찾기

# 퀴즈
# 정수를 입력 받는 input 함수를 5회 호출해서 최대값을 구하세요
def max_5():
    x0 = int(input())   # 정수 최솟값은 -무한 이므로 하나를 잡음
    for _ in range(4):
        x = int(input())
        if max(x0,x) == x: x0 = x

    return x0

# print(max_5())

# 퀴즈
# 정수를 입력 받는 input 함수를 1회 이상 호출해서 최대값을 구하세요

def max_n(number):
    x0 = int(input())

    for _ in range(number-1):
        x = int(input())
        if x > x0: x0 = x

    return x0

n  = int(input('input할 횟수를 입력해주세요 :'))
print(max_n(n))





