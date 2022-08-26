# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.


# dfs --- 시간초과
# dfs로 그래프를 탐색한다.
import sys

sys.setrecursionlimit(10000)
def dfs(start, depth):

    #해당 노드 방문체크 한다.
    visited[start] = True

    # 해당 시작점을 기준으로 계속해서 dfs로 그래프를탐색한다.
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 i번째 노드를 방문하지 않았다면
        if not graph[i]:  # 만약 해당 정점이 연결된 그래프가 없다면
            count += 1  # 개수를 + 1
            visited[i] = True  # 방문 처리
        else:  # 연결된 그래프가 있다면
            dfs(i, 0)  # dfs탐색을 돈다.
            count += 1  # 개수를 +1

print(count)

# bfs
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.

print(count)

# 긁풀이
import sys
sys.setrecursionlimit(10000) # recursion error 발생
input = sys.stdin.readline

N, M = map(int, sys.stdin.readline().split()) # N, M 입력 

graph = [[] for _ in range(N+1)] # 그래프 생성
graph[0] = [0,0]
visited = [False for _ in range(N+1)] # 방문 노드 설정
cnt = 0 # 컴포넌트 개수

for _ in range(M): 
    start, end = map(int, input().split()) # 간선 시점 종점 입력
    graph[start].append(end) # 연결리스트에 추가
    graph[end].append(start)
    graph[start].sort() # 정렬
    graph[end].sort()

def DFS(graph, start, visited): # DFS시작
    visited[start] = True # 방문했으니 True
    for i in graph[start]: # graph 의 점에 연결되있는 점에 대해서
        if not visited[i]: # 방문하지 않은 인접노드라면
            DFS(graph, i, visited) # 방문
for i in range(1, len(visited)): # 1부터 전부 방문
    if visited[i] == False: # 만약 안 갔던 점이라면
        cnt += 1 # 카운트늘리기
        DFS(graph, i, visited) # DFS돌리면서 컴포넌트 추가
print(cnt) # 출력