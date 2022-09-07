# 로봇은 명령어를 읽어들여 정사각형 영역 S를 x축 또는 y축과 평행한 방향으로 움직인다. S의 왼쪽 아래 꼭짓점은 (0, 0)이고, 오른쪽 위의 꼭짓점은 (M, M)이다. 처음에 로봇은 (0, 0)에 위치해 있고, 동쪽 방향을 향하고 있다.

# 명령어는 로봇이 현재 위치에서 행할 동작과 그 동작과 관련된 값으로 주어진다. 동작은 두 가지가 있는데, TURN과 MOVE이다. TURN 0 명령은 현재 위치에서 왼쪽으로 90도 회전, TURN 1 명령은 현재 위치에서 오른쪽으로 90도 회전을 의미한다. MOVE d 명령은 로봇이 향하고 있는 방향으로 d만큼 움직이는 것을 의미한다. 여기서 d는 양수이다.

# 명령의 수행 후 로봇이 S의 경계 또는 내부에 있으면 이 명령어는 유효하다. 만일 명령어 수행 후 로봇이 S의 바깥으로 완전히 나가게 된다면 명령어는 유효하지 않다. 일련의 명령어 열을 이루는 각 명령어가 모두 유효하다면, 이 명령어 열을 유효하다고 한다.

# 한 변의 길이가 M인 정사각형과 n개의 명령어, 그리고 로봇이 (0, 0) 위치에서 시작해 동쪽을 바라보고 있을 때, n개의 명령어를 따라 움직였을 때 최종 위치를 출력하는 프로그램을 작성하라.

# 런타임에러


M, n = map(int, input().split())
dx=[1,0,-1,0] # 하 좌 상 우 : 왼쪽은 좌회전 오른쪽은 우회전
dy=[0,-1,0,1] # 우 하 좌 상
start = [0,0]
result = True
idx = 0
for _ in range(n):
    order, num = input().split()
    if order == 'TURN' and num == '1':
        idx +=1
        if idx >3:
            idx = 0
    if order == 'TURN' and num == '0':
        idx -=1
        if idx == 0:
            idx == 3
    if order == 'MOVE':
        start[0] += dx[idx]*int(num)
        start[1] += dy[idx]*int(num)
    if start[0] <0 or start[0] >M or start[1]<0 or start[1]>M:
        result = False
if result == True:
    print(start[0],start[1])
else:
    print('-1')

# BFS

from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]
def bfs():
    q = deque()
    q.append([startX - 1, startY - 1, startD, 0])
    visit = [[[0 for i in range(5)] for i in range(n)] for i in range(m)]
    visit[startX - 1][startY - 1][startD] = 1
    while q:
        x, y, d, cnt = q.popleft()
        if x == endX - 1 and y == endY - 1 and d == endD: return cnt
        nx, ny = x, y
        for i in range(3):
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny][d] == 1: continue
            if 0 <= nx < m and 0 <= ny < n and s[nx][ny] != 1:
                visit[nx][ny][d] = 1
                q.append([nx, ny, d, cnt + 1])
            else: break
        for i in range(1, 5):
            if d != i and visit[x][y][i] == 0:
                visit[x][y][i] = 1
                if (d == 1 and i == 2) or (d == 2 and i == 1) or (d == 3 and i == 4) or (d == 4 and i == 3):
                    q.append([x, y, i, cnt + 2])
                else:
                    q.append([x, y, i, cnt + 1])
m, n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
startX, startY, startD = map(int, input().split())
endX, endY, endD = map(int, input().split())
print(bfs())