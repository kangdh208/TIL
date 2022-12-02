import sys

input = sys.stdin.readline

# 런타임 에러
N = int(input())
lst = [[input().rstrip()] for _ in range(N)]
lst2 = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            if lst[j][k] == "Y" or (lst[j][i] == "Y" and lst[i][k] == "Y"):
                lst2[j][k] = 1
rst = 0
for q in lst2:
    rst = max(rst, sum(q))
print(rst)

# 긁풀
N = int(input())
v = [[0] * N for _ in range(N)]


def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if g[i][j] == "Y" or (g[i][k] == "Y" and g[k][j] == "Y"):
                    v[i][j] = 1


g = []
for _ in range(N):
    g.append([input()])
floyd()
result = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if v[i][j] == 1:
            cnt += 1
    result = max(result, cnt)

print(result)

# 긁풀
n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):  # 모든 경우 탐색
    friend = 0
    for j in range(n):  # i와 j가 친구인가?
        if i == j:
            continue  # 나는 나와 친구가 될 수 없다...
        if arr[i][j] == "Y":  # i와 j가 친구다
            friend += 1
        elif arr[i][j] == "N":  # i와 j가 친구가 아니다
            for k in range(n):  # j의 친구들 탐색
                if arr[j][k] == "Y" and arr[i][k] == "Y":  # j와 k가 친구고, i와 k도 친구다
                    friend += 1
                    break  # 2-친구가 한 명이라도 있으면 더 찾지 않는다
    answer = max(answer, friend)
print(answer)
