# 22_01_practice.py
import csv_module


# 퀴즈
# weather.csv 파일을 읽고 wf 칼럼에 속한 값들에 대해 빈도를 구하기
# 파일 읽기, 칼럼 추출, 빈도

# 파일 읽기
rows = csv_module.read_weather('data/weather.csv')
# print(*rows, sep='\n')

# 칼럼 추출
wf_items = [row[4] for row in rows]
print(wf_items)

# print(set(wf_items))    # {' 흐림', ' 구름많음', ' 맑음'}

freq = [0, 0, 0]
for wf in wf_items:
    # print(wf)
    if wf == ' 구름많음':
        freq[0] += 1
    elif wf == ' 흐림':
        freq[1] += 1
    else:       # 맑음
        freq[2] += 1

print(freq)

# set은 순서를 보장하지 않는다. sorted로 정렬하자.

labels = sorted(set(wf_items))  # 이렇게 했기 때문에 유니크로 정렬 가능
freq = [0] * len(labels)
for wf in wf_items:
    # print(wf)
    # if wf == labels[0]:
    #     freq[0] += 1
    # elif wf == labels[1]:
    #     freq[1] += 1
    # else:       # 맑음
    #     freq[2] += 1
    for j in range(len(labels)):
        if wf == labels[j]:
            freq[j] += 1

print(freq)

# 데이터 찾는건 어떻게?
def column_index(target):
    names = ['prov', 'city']
    return names.index(target)

# 빈도
# 리스트는 존재하지 않는 곳에 값을 넣을 수 없지만,
# dict는 가능하다. ex) dict['맑음'] == 0
freq_dict = {}
for key in wf_items:
    if key not in freq_dict:
        freq_dict[key] = 0

    freq_dict[key] += 1

# for key in wf_items:
#     if key not in freq_dict:
#         freq_dict[key] = 1
#     else:
#         freq_dict[key] += 1

print(freq_dict)























