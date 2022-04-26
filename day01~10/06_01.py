# 06_01.py


# 퀴즈
# 양의 실수 a에 들어있는 값 중에서 정수 부분만 추출하세요

a = 3.41

# 1. int 형으로 변환
print(int(a))

# 2. 몫 연산하기
print(a//1)

# 3. 소숫점 빼기
print(a - a%1)


# 퀴즈
# 양의 정수 b가 3의 배수이거나 5의 배수인지 알려주세요
# 2개만 표시하면된다

b = 31

if b % 3:
    if b % 5:
        print('3의 배수도, 5의 배수도 아닙니다.')
    else:
        print('5의 배수입니다')
else:
    if b % 5:
        print('3의 배수입니다')
    else:
        print('3의 배수이면서 5의 배수입니다')

# 2개만 표시
if b%5 and b%3: print('3의 배수와 5의 배수 모두 아닙니다')
else : print('3의 배수이거나 5의 배수입니다')

# 만약 안쓴다면?
print(b % 3 == 0 or b % 5 == 0)

print('-'*30)
# 퀴즈
# 정수 c가 음수인지 0인지 양수인지 알려주세요

c = 0
if c:
    if c>0:
        print('양수입니다')
    else:
        print('음수입니다')
else:
    print('0입니다')

# 인터프린터, 컴파일러
# 내가 입력하는걸 무시하는 것 : 공백
#   공백의 종류 : 탭, 스페이스바, 엔터
# 슈도코드 : 가짜코드 x) 음수면 1 빼고 양수면 10 더함 이렇게 말로 함