# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때, S에 정확히 두 개의 서로 다른 문자가 등장하고, 각 문자가 정확히 두 번 등장하는 지 판별하라.

T = int(input())
dic = {}
for z in range(T):
    line = list(input())
    dic = sorted(line)
    if dic[0]==dic[1] and dic[2]==dic[3] and dic[1]!=dic[2]:
        print(f'#{z+1} Yes')
    else:
        print(f'#{z+1} No')