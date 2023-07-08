# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

def DFS(v):
    visited[v]=1
    dfs.append(v)
    for i in node[v]:
        if (visited[i]==0):
            DFS(i)

def BFS(v):
    visited[v]=1
    bfs.append(v)
    queue = [v]

    while(queue):
        for i in node[queue.pop(0)]:
            if(visited[i]==0):
                visited[i]=1
                bfs.append(i)
                queue.append(i)

N, M, V = map(int, input().split())

node =[[]for _ in range(N+1)]
visited = [0]*(N+1)
dfs = []
bfs = []

for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(N+1):
    node[j].sort()

DFS(V)
for j in range(N+1):
    visited[j]=0
BFS(V)

for m in dfs:
    print(m, end=' ')
print()
for n in bfs:
    print(n, end=' ')