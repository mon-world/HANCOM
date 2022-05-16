# 19_02_kma.py
import requests
import re

f = open('data/weather.csv', 'w', encoding='utf-8') # 'w'는 삭제하고 다시 만듦

# 퀴즈
# 기상청 데이터에서 province 태그 안쪽의 내용만 출력하세요
url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
response = requests.get(url)
# print(response)
# print(response.text)

# print(re.findall(r'<province>서울ㆍ인천ㆍ경기도</province>', response.text))
# print(re.findall(r'<province>([ㆍ가-힣]+)</province>', response.text))
# print(re.findall(r'<province>(.+)</province>', response.text))

# 퀴즈
# 기상청 데이터에서 location 태그 안쪽의 내용만 검색하세요
# re.DOTALL - 검색 대상이 여러 줄에 걸쳐있을 때 사용
#             개행문자를 무시하고 검색(전체 문자열을 한 줄로 생각)
# .+  : 탐욕적(greedy)
# .+? : 비탐욕적(non-greedy)
locations = re.findall(r'<location wl_ver="3">(.+?)</location>', response.text, re.DOTALL)
print(len(locations))

# 퀴즈
# location 데이터에서 province, city, data 태그를 검색하세요
for loc in locations:

    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    # print(prov[0], city[0])

    # 퀴즈
    # province와 city를 한번에 검색하세요
    # 18일차 도서관 보기
    # prov_city = re.findall(r'{<province>(.+)</province><city>(.+)</city>}', loc, re.DOTALL)
    # 위 식은 안됨. re.DOTALL 붙혀줘야함. 저 사이에 많은 데이터가 있으므로.
    # 출력모양을 그대로 봐서, 보기
    # print([response.text])
    # prov_city = re.findall(r'{<province>(.+)</province>\r\n\t\t\t\t\t<city>(.+)</city>}', loc, re.DOTALL)
    # 잘 모르니까 .+ 쓰고 원하지 않는 것이기 때문에 ()를 쓰지 않는다.
    prov_city = re.findall(r'<province>(.+)</province>.+<city>(.+)</city>', loc, re.DOTALL)

    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)

    # 퀴즈
    # data 태그 데이터에서 mode, tmEf, wf, tmn, tmx, rnSt 태그를 검색하기
    # 출력 : A02, 2022-05-16 00:00, 맑음, 12, 24, 0
    for datum in data:
        # mode = re.findall(r'<mode>(.+)</mode>', datum)
        # tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        # wf = re.findall(r'<wf>(.+)</wf>', datum)
        # tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
        # tmx = re.findall(r'<tmx>(.+)</tmx>', datum)
        # rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)
        #
        # print(mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0])

        # 퀴즈
        # findall 1번 사용
        # all_data = re.findall(r'<mode>(.+)</mode>.+<tmEf>(.+)</tmEf>.+<wf>(.+)</wf>.+<tmn>(.+)</tmn>.+<tmx>(.+)</tmx>.+<rnSt>(.+)</rnSt>', datum, re.DOTALL)
        # mode, tmEf, wf, tmn, tmx, rnSt = all_data[0]
        # print(mode, tmEf, wf, tmn, tmx, rnSt)

        # 돌아만 감
        # 안에 있는 글자만 다름
        # dotall 필요 없음. 같은 라인만 찾기 때문.
        '''
        # 여긴 왜 [0]이 아닌것인가...????????
        '''
        all_data2 = re.findall(r'<.+>(.+)<.+>', datum)
        mode, tmEf, wf, tmn, tmx, rnSt = all_data2
        # print(prov, city, mode, tmEf, wf, tmn, tmx, rnSt)

        # 아래가 깔끔하지만 위가 어떤 데이터인지 더 선명함


        # data 안에 검색해보면 mode~rnSt 1개씩 있음.


        # 한번에 하나씩 써야함. 그게 귀찮음.
        # 개행문자 필요
        f.write('{}, {}, {}, {}, {}, {}, {}, {}\n'.format(prov, city, mode, tmEf, wf, tmn, tmx, rnSt))

# 제주도 서귀포
# A02 2022-05-19 00:00 구름많음 17 23 30
# A02 2022-05-19 12:00 구름많음 17 23 30

# 영구적으로 저장할 수 있어야함.
# 이대로 하면 json 형식이 아니어서 전송이 힘들 수 있음.
# json의 치명적 결함 : 가독성 떨어짐. 줄바꿈이 없음. 원래는 1줄로 쭉 가있음.
# 단점 : 사람이 보는 데이터라 기계가 해석하기 힘듦. 특정한 영역 읽어오기 힘듦.
# 원하는 것을 찾기 힘듦.

# 제주도 서귀포 A02 2022-05-19 00:00 구름많음 17 23 30
# 이런 식이면 앞에 제주도 서귀포만 찾으면 바로 뒤에 긁어오면 된다.
# 단, 파일 용량이 커진다. 하지만 처리하기 편한게 좋음.


# 퀴즈
# 기존 출력 행태를 개선된 형태로 수정하기
# 제주도 서귀포 A02 2022-05-19 00:00 구름많음 17 23 30
# print(prov_city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0])
print(prov_city)

# 퀴즈
# 기상청으로부터 수신한 데이터를 weather.csv 파일로 저장하기.
f.close()