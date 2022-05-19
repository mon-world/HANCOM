# 22_03_class.py

# 프로그램 : 코드(함수), 데이터(변수)
# 클래스 : 함수와 변수가 같이 있는 것. 서로 관련이 되어있다. 서로 같이 사용된다.
# 즉 함수와 변수를 묶어주는 역할.

# 클래스 안에 함수 : 멤버 함수


class Info:  # 함수와 변수가 들어간다.
    age = 23  # 정적 맴버변수

    def __init__(self, name):  # 함수(매개변수)
        print('init')
        self.name = name  # 지역변수 : 함수 안에서 사용한건 함수에서만 사용한다.

    def show(self):  # 매개변수명을 바꿀 수 있으나 놔둔다.
        print('hello', self.name)


a = Info("kim")  # 생성자 호출. : 클래스를 완벽하게 만듦
# () : 함수를 호출하는 코드.

# a.show()

# self는 info가 아니라 a다.

b = Info("Yang")  # 이 땐 self는 a인지 b인지 모른다. show 호출 방법이 한가지 더 생김

# 객체지향 프로그램은 철학.
# 묶어서 전달하는 것이 가장 쉽다.

# b.show(123) # 123은 나 자신이 아니기 때문에 틀린 코드
a.show()
Info.show(a)

# 퀴즈
# 리스트를 정렬(2가지)
# ns = [1, 2, 5, 8, 12]
#
# ns.sort()
# list.sort(ns)
# print(ns)
#
# print(a.age)
# print(Info.age)         # 이 표현이 더 정확

# 클래스 호출하는 방법이 2가지이다 라는걸 이해

# 서로 저장하는 데이터가 다르다.
# a.age = 31
# b.age = 45
# print(a.age)
# print(b.age)
# print(Info.age)

# self는 a,b,c,... 모두 된다.
# print(Info.name)    # 에러.
# print(a.name)
#
#
# a.addr = "1"
# print(a.addr)

# show가 올바르게 되려면???
print(a.show())


'''
변수를 age처럼 선언하면 1번밖에 선언 안된다.
a,b,c에도 나이가 있어야하는데 클래스 전체에 있는 전역변수이다.

a,b,c들이 모두 거치는 init 안에 만들어야하는데,
그 안에 만들면 변수 만드는 코드가 실행이된다. 중요.
name = 'kim'이라 하면
self : a,b,c에다 만들겠다는 것.
이렇게 하면 모든 객체가 동일하게 name 이라는 변수를 가지게 됨. 중요.
'''