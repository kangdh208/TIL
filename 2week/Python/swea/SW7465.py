# 창용 마을에는 N명의 사람이 살고 있다.

# 사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.

# 두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.

# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,

# 이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.

# 창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.

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

T = int(input())
for z in range(1,T+1):
    N, M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == False:
            cnt += 1
            visited[i] = True
            bfs(i)
    print(f'#{z} {cnt}')