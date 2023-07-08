# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ans = [1] * N
for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i]:
            ans[i] = max(ans[j] + 1, ans[i])
print(max(ans))
