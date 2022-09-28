# 우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.


# BFS
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) # recursionerror 방지

n = int(input())
a, b = map(int, input().split()) 
m = int(input())
graph = [[] for _ in range(n+1)] # graph 설정
visited = [False] * (n+1) # 방문노드파악 설정
for i in range(m): # 인접 리스트 생성
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque()
q.append((0, a)) # 시작점을 a 추가
def bfs(): # BFS 시작
    while q: #
        d, x = q.popleft() # x 제거
        visited[x] = True # x 방문노드 추가
        for i in graph[x]: # 그래프에서 x의 인접중에 
            if not visited[i]: # 방문안했다면
                q.append((d+1, i)) # 큐에 추가
            if i == b: # 종점이라면
                return d+1 # 지금까지 쌓인 d 반환
    return -1 # 아무것도 없으면 -1 반환
print(bfs())

# DFS

import sys
sys.setrecursionlimit(300000)

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)
            
n = int(input())
graph = [[] for _ in range(n+1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
dfs(s)
print(check[e] if check[e] > 0 else -1)