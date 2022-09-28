# 오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

# 깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }

# 런타임에러
N, M, R = map(int, input().split())
board = [[]*N for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)
for i in range(M):
    board[i].sort()
visited = [False]*(N+1)
lst = [0] * N
def dfs(start):
    visited[start] = True
    lst[start-1] = start
    for i in board[start]:
        if visited[i] == False:
            dfs(i)
dfs(R)
print(*lst, sep='\n')

