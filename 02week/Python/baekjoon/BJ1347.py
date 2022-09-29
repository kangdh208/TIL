# 홍준이는 미로 안의 한 칸에 남쪽을 보며 서있다. 미로는 직사각형 격자모양이고, 각 칸은 이동할 수 있거나, 벽을 포함하고 있다. 모든 행과 열에는 적어도 하나의 이동할 수 있는 칸이 있다. 홍준이는 미로에서 모든 행과 열의 이동할 수 있는 칸을 걸어다녔다. 그러면서 자신의 움직임을 모두 노트에 쓰기로 했다. 홍준이는 미로의 지도를 자기 노트만을 이용해서 그리려고 한다.

# 입력으로 홍준이가 적은 내용을 나타내는 문자열이 주어진다. 각 문자 하나는 한 번의 움직임을 말한다. ‘F’는 앞으로 한 칸 움직인 것이고, ‘L'과 ’R'은 방향을 왼쪽 또는 오른쪽으로 전환한 것이다. 즉, 90도를 회전하면서, 위치는 그대로인 것이다.

import sys

input = sys.stdin.readline

N = int(input())
way = input().strip()
position = [(0, 0)]
dx = [-1, 0, 1, 0]  # 상 우 하 좌
dy = [0, 1, 0, -1]  # 북 동 남 서
dl = 2
for i in way:
    if i == "R":
        dl = (dl + 1) % 4
    elif i == "L":
        if dl != 0:
            dl = (dl - 1) % 4
        else:
            dl = 3
    else:
        x = position[-1][0] + dx[dl]
        y = position[-1][1] + dy[dl]
        position.append((x, y))
# x, y 의 최대 최소 구하기
x_sort = sorted(position, key=lambda x: x[0])
y_sort = sorted(position, key=lambda x: x[1])
x_min, x_max = x_sort[0][0], x_sort[-1][0]
y_min, y_max = y_sort[0][1], y_sort[-1][1]

# 2차원 배열 만들기
maze = [["#" for y in range(y_min, y_max + 1)] for x in range(x_min, x_max + 1)]

# 음수가 나올 수 있으므로 최소값만큼 더해주기 ( 양수로 바꾸기 )
for i in range(len(position)):
    position[i] = (position[i][0] - x_min, position[i][1] - y_min)

# 좌표로 길 만들기
for i, j in position:
    maze[i][j] = "."

# 답
for row in maze:
    print("".join(row))
