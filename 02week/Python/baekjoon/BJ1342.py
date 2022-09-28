# 민식이와 준영이는 자기 방에서 문자열을 공부하고 있다. 민식이가 말하길 인접해 있는 모든 문자가 같지 않은 문자열을 행운의 문자열이라고 한다고 한다. 준영이는 문자열 S를 분석하기 시작했다. 준영이는 문자열 S에 나오는 문자를 재배치하면 서로 다른 행운의 문자열이 몇 개 나오는지 궁금해졌다. 만약 원래 문자열 S도 행운의 문자열이라면 그것도 개수에 포함한다.

import sys

input = sys.stdin.readline


def dfs(pre_word, picked):

    if picked == len(S):
        return 1
    answer = 0
    for key in counter.keys():
        if pre_word == key:
            continue
        if counter[key] == 0:
            continue
        counter[key] -= 1
        answer += dfs(key, picked + 1)
        counter[key] += 1
    return answer


S = list(input().strip())
counter = dict()
for s in S:
    if s in counter:
        counter[s] += 1
    else:
        counter[s] = 1

answer = dfs("", 0)
print(answer)
