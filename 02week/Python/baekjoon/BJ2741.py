# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline
n = int(input())
i = 1
while i<=n:
    print(i)
    i += 1
