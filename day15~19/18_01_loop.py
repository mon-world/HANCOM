# 퀴즈
# 원금이 2배 되는 기간
# 연 복리

def how_many_years(money, interest):
    period = 0
    money_first = money
    while money <= 2*money_first:
        period += 1
        money *= 1+interest

    return period

print(how_many_years(1, 0.01))