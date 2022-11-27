# M개의 자연수로 이루어진 집합 S와 자연수 N이 주어진다.

# S에 속하지 않는 자연수 x, y, z를 골라서, |N - xyz|의 최솟값을 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
if M != 0:
    lst = list(map(int, input().split()))
else:
    lst = input()
ans = N
for i in range(1000):
    if lst[i] == 1:
        continue
    for j in range(i + 1, 1000):
        if lst[j] == 1:
            continue
        for k in range(k + 1, 1000):
            if lst[k] == 1:
                continue
            ans = min(ans, abs(N - i * j * k))
print(ans)
