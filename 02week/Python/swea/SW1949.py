# 등산로를 조성하려고 한다.

# 등산로를 만들기 위한 부지는 N * N 크기를 가지고 있으며, 이곳에 최대한 긴 등산로를 만들 계획이다.

# 등산로 부지는 아래 [Fig. 1]과 같이 숫자가 표시된 지도로 주어지며, 각 숫자는 지형의 높이를 나타낸다.
# 등산로를 만드는 규칙은 다음과 같다.

#    ① 등산로는 가장 높은 봉우리에서 시작해야 한다.

#    ② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
#        즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.

#    ③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.

# N * N 크기의 지도가 주어지고, 최대 공사 가능 깊이 K가 주어진다.

# 이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하는 프로그램을 작성하라.

# [제약 사항]

# 1. 시간 제한 : 최대 51개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초

# 2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)

# 3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)

# 4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.

# 5. 지도에서 가장 높은 봉우리는 최대 5개이다.

# 6. 지형은 정수 단위로만 깎을 수 있다.

# 7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.

dr = [-1,0,1,0] # 상 우 하 좌
dc = [0,1,0,-1]

def dfs(row,col,path,construct):
    global ans
    if ans < path: # 등산로 갱신
        ans = path
    for k in range(4): # 델타탐색
        nrow = row+dr[k]
        ncol = col+dc[k]
        if nrow<0 or nrow>=N or ncol<0 or ncol>=N:
            continue # 영역벗어나면 패스
        if visited[nrow][ncol] == 1:
            continue
        if mountain[row][col]>mountain[nrow][ncol]:
            visited[nrow][ncol] = 1 #이동가능하면
            dfs(nrow,ncol,path+1,construct) # 재귀호출
            visited[nrow][ncol] = 0 # 갔다오면 초기화
        elif mountain[row][col]<=mountain[nrow][ncol] and construct ==False: # 이동불가능하면
            for i in range(1,K+1):
                mountain[nrow][ncol]-=i # 공사해보기
                construct = True
                if mountain[row][col]>mountain[nrow][ncol]:
                    visited[nrow][ncol] =1
                    dfs(nrow,ncol,path+1,construct)
                    visited[nrow][ncol] = 0
                construct = False # 다른경우 확인 위해
                mountain[nrow][ncol] += i # 공사 취소

T = int(input())
for z in range(T):
    N,K = map(int,input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    top = 0 # 정상 찾기
    for i in range(N):
        for j in range(N):
            if top < mountain[i][j]:
                top = mountain[i][j]
    ans = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == top: # 정상높이랑 같으면
                visited = [[0]*N for _ in range(N)]
                visited[i][j] = 1 
                dfs(i,j,1,False) # 등산로 탐색
    print(f'#{z+1} {ans}')