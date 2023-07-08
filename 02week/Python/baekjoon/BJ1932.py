#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5
# 위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

# 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

# 삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.


# Top Down
import sys

input = sys.stdin.readline
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            lst[i][0] += lst[i - 1][0]
        elif j == i:
            lst[i][j] += lst[i - 1][j - 1]
        else:
            lst[i][j] += max(lst[i - 1][j - 1], lst[i - 1][j])
print(max(lst[-1]))

# Bottom Up

N = int(input())


def func(i, j):
    if i == N - 1:
        return lst[i][j]
    if not dp[i][j]:
        dp[i][j] = max(func(i + 1, j), func(i + 1, j + 1)) + lst[i][j]
    return dp[i][j]


lst = [list(map(int, input().split())) for _ in range(N)]
dp = []
for i in range(1, N + 1):
    dp.append([0 for _ in range(i)])
print(func(0, 0))
