# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

# DFS
import sys
sys.setrecursionlimit(10000) # recursion error 방지

# 시계 방향
dX = [1, 1, 0, -1, -1, -1, 0, 1]
dY = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    def DFS(x, y, mapList, visitedList):
        visitedList[y][x] = True  # 방문 완료

        for i in range(8): # 델타 탐색
            nx = x + dX[i]
            ny = y + dY[i]

            if 0 <= nx < w and 0 <= ny < h:
                if visitedList[ny][nx] == False and mapList[ny][nx] == 1:
                    DFS(nx, ny, mapList, visitedList)

    w, h = map(int, input().split())
    if w == 0 and h == 0: # 입력 종료
        break

    mapList = [] # 지도생성하기
    for i in range(h):
        mapList.append(list(map(int, input().split())))
    visitedList = [list(False for _ in range(w)) for _ in range(h)] # 방문노드 : all False

    count = 0 

    for i in range(h):
        for j in range(w):
            if visitedList[i][j] == False and mapList[i][j] == 1: # 방문안했고 육지라면
                DFS(j, i, mapList, visitedList) # 섬인지 확인
                count += 1

    print(count)

# BFS
from collections import deque
import sys
sys.setrecursionlimit(10000)

# 시계 방향
dX = [1, 1, 0, -1, -1, -1, 0, 1]
dY = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    def DFS(x, y, mapList, visitedList):
        visitedList[y][x] = True  # 방문 완료

        for i in range(8):
            nX = x + dX[i]
            nY = y + dY[i]

            if 0 <= nX < w and 0 <= nY < h:
                if visitedList[nY][nX] == False and mapList[nY][nX] == 1:
                    DFS(nX, nY, mapList, visitedList)

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    mapList = []
    for i in range(h):
        mapList.append(list(map(int, input().split())))
    visitedList = [list(False for _ in range(w)) for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if visitedList[i][j] == False and mapList[i][j] == 1:
                DFS(j, i, mapList, visitedList)
                count += 1

    print(count)