# 오목은 바둑판에 검은 바둑알과 흰 바둑알을 교대로 놓아서 겨루는 게임이다. 바둑판에는 19개의 가로줄과 19개의 세로줄이 그려져 있는데 가로줄은 위에서부터 아래로 1번, 2번, ... ,19번의 번호가 붙고 세로줄은 왼쪽에서부터 오른쪽으로 1번, 2번, ... 19번의 번호가 붙는다.

# 입력으로 바둑판의 어떤 상태가 주어졌을 때, 검은색이 이겼는지, 흰색이 이겼는지 또는 아직 승부가 결정되지 않았는지를 판단하는 프로그램을 작성하시오. 단, 검은색과 흰색이 동시에 이기거나 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 입력으로 들어오지 않는다.





dx = [-1,0,1,1] #좌하,하,우,우하
dy = [1,1,0,1] #동일
board = []
for _ in range(19):
    board.append(list(map(int, input().split())))
result = 0


def chk(x, y):
    color = board[x][y] # 흑 백

    # 방향 탐색
    for k in range(4):
        cnt = 1 # 몇목인지 세기
        nextx = x + dx[k]
        nexty = y + dy[k]

        # 오목이 되는지 확인
        while 0 <= nextx < 19 and 0 <= nexty < 19 and board[nextx][nexty] == color:
            cnt += 1

            # 오목?
            if cnt == 5:
                # 육목 체크
                if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and board[x - dx[k]][y - dy[k]] == color:
                    break
                if 0 <= nextx + dx[k] < 19 and 0 <= nexty + dy[k] < 19 and board[nextx + dx[k]][nexty + dy[k]] == color:
                    break

                # 육목이 아니면
                # 바둑알의 색과 위치를 출력 후 종료
                print(color)
                print(x + 1, y + 1)
                exit(0)

            # 이전에 이동했던 방향으로 다시 이동
            nextx += dx[k]
            nexty += dy[k]




# 반복문을 통해 바둑알이 있는 위치를 탐색
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            chk(i, j)

print(0)