# N×M크기의 배열로 표현되는 미로가 있다.
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y)) # 현위치
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x+dx[k] # 상하좌우
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<M: #범위내에 있으면
                if board[nx][ny] == 1: # 처음방문이면
                    board[nx][ny] = board[x][y] +1 #최단거리
                    queue.append((nx,ny))# 기록
    return board[N-1][M-1]


N,M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input())))

print(bfs(0,0))