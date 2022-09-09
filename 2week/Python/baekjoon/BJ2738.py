# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lstA = []
lstB = []
for _ in range(N):
    lstA.append(list(map(int,input().split())))
for _ in range(N):
    lstB.append(list(map(int,input().split())))
for i in range(N):
    for j in range(M):
        lstA[i][j] = lstA[i][j] + lstB[i][j]
for i in range(N):
    print(' '.join(map(str,lstA[i])))