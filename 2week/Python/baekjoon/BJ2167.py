# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.


# 시간초과
from pprint import pprint
import sys
input = sys.stdin.readline

N, M  = map(int,input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    numsum = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            numsum += board[a][b]
    print(numsum)

# 동적할당
# 배열 입력
N, M = map(int, input().split())
numboard = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
# 합산판 생성 idx범위 고려해서 1씩 늘리기

sumboard = [[0] * (M+1) for _ in range(N+1)] # 뒤에 -1 위해서 미리 1 추가 입력
pprint(numboard)
pprint(sumboard)
# 합산 입력
for i in range(1, N+1):
    for j in range(1, M+1):
        sumboard[i][j] = numboard[i-1][j-1] + sumboard[i][j-1] + sumboard[i-1][j] - sumboard[i-1][j-1]
# 입력과 출력
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(sumboard[x][y] - sumboard[x][j-1] - sumboard[i-1][y] + sumboard[i-1][j-1])