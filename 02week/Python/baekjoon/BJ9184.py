# 재귀 호출만 생각하면 신이 난다! 아닌가요?

# 다음과 같은 재귀함수 w(a, b, c)가 있다.

# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1

# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)

# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
# 위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)

# a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
import sys

input = sys.stdin.readline

lst = [[[0] * (21) for _ in range(21)] for _ in range(21)]


def w(p, q, r):
    if p <= 0 or q <= 0 or r <= 0:
        return 1
    if p > 20 or q > 20 or r > 20:
        return w(20, 20, 20)
    if lst[p][q][r]:
        return lst[p][q][r]
    if a < b < c:
        lst[p][q][r] = w(p, q, r - 1) + w(p, q - 1, r - 1) - w(p, q - 1, r)
        return lst[p][q][r]
    lst[p][q][r] = (
        w(p - 1, q, r)
        + w(p - 1, q - 1, r)
        + w(p - 1, q, r - 1)
        - w(p - 1, q - 1, r - 1)
    )
    return lst[p][q][r]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a,b,c)}")

# 긁풀 2
import sys

input = sys.stdin.readline


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[a][b][c]
    dp[a][b][c] = (
        w(a - 1, b, c)
        + w(a - 1, b - 1, c)
        + w(a - 1, b, c - 1)
        - w(a - 1, b - 1, c - 1)
    )
    return dp[a][b][c]


dp = [[[0] * (21) for _ in range(21)] for _ in range(21)]
# 0~20까지므로

while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")


import sys

input = sys.stdin.readline


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if board[a][b][c]:
        return board[a][b][c]
    if a < b < c:
        board[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return board[a][b][c]
    else:
        board[a][b][c] = (
            w(a - 1, b, c)
            + w(a - 1, b - 1, c)
            + w(a - 1, b, c - 1)
            - w(a - 1, b - 1, c - 1)
        )
        return board[a][b][c]


board = [[[0] * 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
