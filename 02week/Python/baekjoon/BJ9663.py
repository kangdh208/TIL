# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

from pprint import pprint


# class Solution:
#     def solveNQueens(self, n):
#         def DFS(queens, xy_dif, xy_sum):
#             """
#             temp = [["." * i + "Q" + "." * (n - i - 1) for i in queens]]
#             for t in temp:
#                 for tt in t:
#                     print(tt)
#                 print("\n")
#             print("\n")
#             """

#             p = len(queens)  # p is the index of row
#             if p == n:
#                 result.append(queens)
#                 return None
#             for q in range(n):  # q is the index of col
#                 # queens stores those used cols, for example, [0,2,4,1] means these cols have been used
#                 # xy_dif is the diagonal 1
#                 # xy_sum is the diagonal 2
#                 if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
#                     DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

#         result = []
#         DFS([], [], [])
#         return [["□" * i + "■" + "□" * (n - i - 1) for i in sol] for sol in result]


# s = Solution()
# res = s.solveNQueens(int(input()))
# pprint(res)


class Solution:
    def solveNQueens(self, n: int):
        col = set()
        up = set()
        down = set()

        res = []
        chess = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                line = ["".join(row) for row in chess]
                res.append(line)
                return
            for c in range(n):
                if c in col or (r + c) in up or (r - c) in down:
                    continue
                col.add(c)
                up.add(r + c)
                down.add(r - c)
                chess[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                up.remove(r + c)
                down.remove(r - c)
                chess[r][c] = "."

        backtrack(0)
        return res


s = Solution()
res = s.solveNQueens(int(input()))
print(res)


## acmicpc baekjoon pypy3 submit
n = int(input())

ans = 0
row = [0] * n


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(ans)
