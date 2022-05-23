# 25_01_song.py
import requests
# import requests_oauthlib
import re

# get : 주소창, 장점(다루기 쉽다), 단점(길이 제한, 무조건 공개)
# post : 백그라운드. get의 단점을 고려


# 퀴즈
# 한국음악저작권협회로부터 지드래곤의 저작권 데이터를 가져와서 데이터로 변환해서 출력

# 데이터 골라서 가져오기

# payload : 실제데이터
payload = {
    'S_PAGENUMBER': 1,
    'S_MB_CD': 'W0001300',
    'S_HNAB_GBN': 'I',
    'hanmb_nm': '강산에',
    'sort_field': 'SORT_PBCTN_DAY'
}

# 틀린 것.
# 가수에 대한 정보가 들어있지 않음.
# 구글 크롬으로 crtl shift i로 개발자 도구 불러오기 - payload를 추가
url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
response = requests.get(url, data=payload)
print(response)
print(response.text)

# 퀴즈
# 수신한 데이터로부터 저작물명, 가수명, 작사, 작곡, 편곡데이터를 추출하기


# ?의미 : 여러개 존재할 때 필요. td태크는 같은 줄이므로 필요 없음

tbody = re.findall(r'<tbody>(.+?)</tbody>', response.text, re.DOTALL)
# print(len(tbody))
# print(tbody[0])
# print(tbody[1])

trs = re.findall(r'<tr>(.+?)</tr>', tbody[1], re.DOTALL)
# print(len(trs))
# print(trs[0])

# 퀴즈
# tr 태그 안쪽에 있는 td 태그를 찾으세요
for tr in trs:
    # print(tr)
    tds = re.findall(r'<td>(.+)</td>', tr)
    # print(tds)
    # print(tds[1], tds[1].replace('<br/>', ','))

    new_tds = []
    for td in tds:
        td = td.strip()
        td = td.replace('<br/>', ',')
        td = td.replace(' <img src="/images/common/control.gif" alt="" />', '')
        td = td.replace(' <img src="/images/common/control.gif"  alt="" />', '')

        new_tds.append(td)

    print(new_tds)
