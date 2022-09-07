# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
com = 1
for i in range(K):
    mul = N-i
    com *=mul
div =1
for j in range(1,K+1):
    div *=j
print(int(com/div))