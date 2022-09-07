# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
N = int(input())
lst1 = set(map(int, input().split()))
M = int(input())
lst2 = list(map(int, input().split()))
for i in range(M):
    if lst2[i] in lst1:
        print(1)
    else:
        print(0)