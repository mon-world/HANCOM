# 22_02_exception.py : 예외처리


def exception_basic():
    a = [1, 5, 9]
    print(a)

    # 퀴즈
    # input함수로 인덱스를 입력 받아서 리스트로부터 해당 위치의 데이터를 출력하세요

    # n = input('숫자를 입력해주세요: ')
    # print(a[int(n)])

    # 퀴즈
    # 앞에서 만든 코드에 에러 처리를 추가하세요

    # try의 코드만 에러처리 하겠다는 뜻
    # try:
    #     n = int(input('0~2 자연수를 입력해주세요: '))
    #
    #     if not 0 <= int(n) <= 2 and int(n) // 1 == int(n):
    #         print("0~2의 자연수가 아닙니다.")
    #     else :
    #         print(a[int(n)])
    # except ValueError as e:      # 어떤 에러인지 표시
    #     print('에러처리')
    #     print(e)
    #
    # exit()

    # 퀴즈
    # 전통적인 에러 처리 방식을 예외 처리 방식으로 수정하세요
    idx = 1.1
    try:
        print(a[idx])
    except TypeError as e:
        print("범위를 벗어났습니다")
        print(e)


    # 에러 처리 아님. 죽지 않게 만든 것 뿐.


# 퀴즈
# 사용자로부터 정수 1개를 완벽하게 입력받을 수 있는 함수

def input_integer_absolutely():
    while True:
        n = input('숫자를 입력해주세요: ')
        if n == '0':
            return int(n)
        else:
            try:
                return int(n)
            except ValueError as e:
                print('정수가 아닙니다.')
                print(e)

print(input_integer_absolutely())