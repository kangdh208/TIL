# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline
n = int(input())
while n>0:
    print(n)
    n -= 1