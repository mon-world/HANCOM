# 11_03_while.py

# 내부적으로 사용함. for는 사람이 쓰기 편함.
'''
while ?: # 참 반복, 거짓 멈춤
    print('hello')
'''

i = 0
while i < 10:   # i =! 10 쓰지말기
    print(i)
    i += 1

# while문은 for을 사용할 수 없을 때 사용한다.
# for문은 정확한 횟수가 정해지면 한다.
# 단순반복은 while쓰는게 편함
# range 함수로 표현 할 수 없으면 while

# 퀴즈
# input 함수로 0을 입력할 때까지의 합계를 구하세요

x = 0
while True:
    if int(input()) == 0: break
    x += int(input())

print(x)
