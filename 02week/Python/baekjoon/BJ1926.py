# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

dx = [0,0,-1,1] # 좌우상하
dy = [-1,1,0,0]
n,m = map(int, input().split())
paint = []
for _ in range(n):
    paint.append(list(map(int, input().split())))

# 긁풀
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
do = [] # 도화지, 그래프
cnt = 0 # 그림의 갯수 변수
res = [0] # 그림의 넓이 담을 배열

# 그림 그리기
for i in range(n):
    do.append(list(map(int,input().rstrip().split())))
    
def bfs(x,y):
	# 상하좌우 4방향
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append([x,y])
    do[x][y] = 0 # 시작점 방문처리
    are = 1 # 넓이는 1부터 시작
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
			# 도화지 안에 위치하고 아직 방문하지 않았다면 방문
            if 0 <= nx < n and 0 <= ny < m and do[nx][ny] == 1:
                are += 1 # 넓이 키우기
                do[nx][ny] = 0 # 방문 처리            
                queue.append([nx, ny]) # 큐에 삽입
    res.append(are) # 그림의 넓이 배열에 삽입

for x in range(n):
    for y in range(m):
        if do[x][y] == 1: # 그림이 그려져있다면 BFS 탐색 시작
            bfs(x,y)
            cnt += 1 # 그림 갯수 +1

print(cnt) # 그림갯수 출력
print(max(res)) # 그림의 넓이 최대값 출력