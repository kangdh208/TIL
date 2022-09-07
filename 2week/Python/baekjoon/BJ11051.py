# 자연수 N과 정수 K가 주어졌을 때 이항 계수 
# N combination K를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
# 긁풀
N, K = map(int, input().split())
dp = [] # 파스칼 삼각형
for i in range(N+1) :
    dp.append([1]*(i+1))
for i in range(2, N+1) :
    for j in range(1, i) :
        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%10007

print(dp[N][K])

