# 15_01_list.py

import random

def make_randoms(size):
    a = []
    for _ in range(size):
        a.append(random.randrange(100))

    return a


# 퀴즈
# 리스트에서 가장 큰 값의 위치를 알려주는 함수를 만드세요 (find_max_pos)


random.seed(23)
ns = make_randoms(10)
print(ns)

def find_max_pos_my(ns):
    a, pos = ns[0], 0
    for i, k in enumerate(ns):
        if a < i:
            a, pos = i, k

    return pos

print(find_max_pos_my(ns))

# 더 나은 코드
def find_max_pos(ns, size):
    max_pos = 0     # 변수를 줄여라 !
    for i in range(size):
        if ns[max_pos] < ns[i]:     # 초기 0이고, i로 바뀌기 때문에 이렇게 가능
            max_pos = i

    return max_pos

# 퀴즈
# 앞에서 만든 함수를 사용해서 리스트를 오름차순으로 정렬하세요(insertion_sort)
# 설명 잘 들어야 할듯
# 주석은 가능한 한 짧게

def selection_sort(ns):
    # pos = find_max_pos(ns, len(ns) - 0)
    # ns[-1-0], ns[pos] = ns[pos], ns[-1-0]
    #
    # pos = find_max_pos(ns, len(ns) - 1)
    # ns[-1-1], ns[pos] = ns[pos], ns[-1-1]
    #
    # pos = find_max_pos(ns, len(ns) - 2)
    # ns[-1-2], ns[pos] = ns[pos], ns[-1-2]

    for i in range(len(ns)):
        pos = find_max_pos(ns, len(ns) - i)
        ns[-1 - i], ns[pos] = ns[pos], ns[-1 - i]
        print(ns)

print(selection_sort(ns))


