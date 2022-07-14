# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

import sys

input = sys.stdin.readline
n = int(input())
i = 1
while i<=n:
    print('*' * i)
    i+=1