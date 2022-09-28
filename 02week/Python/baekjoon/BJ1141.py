# 접두사X 집합이란 집합의 어떤 한 단어가, 다른 단어의 접두어가 되지 않는 집합이다. 예를 들어, {hello}, {hello, goodbye, giant, hi}, 비어있는 집합은 모두 접두사X 집합이다. 하지만, {hello, hell}, {giant, gig, g}는 접두사X 집합이 아니다.

# 단어 N개로 이루어진 집합이 주어질 때, 접두사X 집합인 부분집합의 최대 크기를 출력하시오.

import sys
input = sys.stdin.readline

N = int(input())

words = [input().rstrip() for _ in range(N)]

words.sort(key=len)
result = 0

for i in range(N):
    chk = False
    for j in range(i+1, N):
        if words[i] == words[j][:len(words[i])]:
            chk = True
            break
    if not chk:
        result +=1
print(result)