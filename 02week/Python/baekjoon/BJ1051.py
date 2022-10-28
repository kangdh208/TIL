# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
answer = []

for i in range(n):
    for j in range(m):
        target = graph[i][j]
        for k in range(j, m):
            if graph[i][k] == target and i + k - j < n and k < m:
                if graph[i + k - j][j] == target and graph[i + k - j][k] == target:
                    answer.append((k - j + 1) ** 2)
print(max(answer))
