# m행 n열로 이루어진 그리드가 주어진다. 일부 칸에는 박스가 들어 있다. 모든 박스가 더 이상 움직일 수 없을 때 까지 아래로 움직인다면, 박스는 쌓여진 상태가 된다.

# 박스가 움직인 거리는 바닥에 쌓이기 전 까지 이동한 칸의 개수이다. 모든 박스가 이동한 거리 (각 박스가 이동한 거리의 합) 을 구하는 프로그램을 작성하시오. 

# 런타임에러

N = int(input())
for _ in range(N):
    m,n = map(int, input().split())
    arr = [[] for _ in range(N)]
    for i in range(m):
        line = list(input().split())
        for j in range(n):
            arr[j].append(line[j])
    cnt = 0
    for i in range(n):
        box = arr[i].count('1')
        base = m-1
        for j in range(m-1,-1,-1):
            if arr[i][j] == '1' :
                cnt += base -j
                base -=1
    print(cnt)

# 팀원풀이
t = int(input())

for tc in range(t):

    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]

    # 전치할 transposed_matrix 리스트에 0으로 초기화
    transposed_matrix = [[0] * m for _ in range(n)]

    # matrix를 전치
    for i in range(n):
        for j in range(m):
            transposed_matrix[i][j] = matrix[j][i]

    # cnt 변수 0으로 초기화
    cnt = 0

    # transposed_matrix 순회
    for i in range(n):
        # 바닥
        floor = m - 1

        # 바닥에서부터 순회
        for j in range(m-1, -1, -1):
            # 값이 1이라면
            if transposed_matrix[i][j] == 1:
                # 바닥 - 현재 위치
                cnt += floor - j
                # 바닥 1 높이기
                floor -= 1

    print(cnt)