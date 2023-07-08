# 세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

# 배열 A와 B의 인덱스는 1부터 시작한다.


import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

start, end = 1, N * N

while start <= end:
    middle = (start + end) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(middle // i, N)
    if cnt >= K:
        end = middle - 1
    else:
        start = middle + 1

print(start)
