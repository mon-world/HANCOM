# 15_02_re.py
import re

db = '''
3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534
'''

# print(db)       # 줄이 바뀌었으니 개행문자(\n) 존재

# 퀴즈
# 모든 숫자를 찾아보세요
# r : raw string
print(re.findall(r'[0-9]', db))     # 숫자 쓰기
print(re.findall(r'[0-9]+', db))    # 번호 찾기. 앞 유닛 1개 이상이란 뜻