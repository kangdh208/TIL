# 스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.

# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.

# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.

def row(lst):
    cnt = 0
    for i in range(9):
        rowlst = []
        for j in range(9):
            rowlst.append(lst[i][j])
        if sorted(rowlst) == [1,2,3,4,5,6,7,8,9]:
            cnt += 1
    if cnt == 9:
        return True

def col(lst):
    cnt = 0
    for i in range(9):
        collst = []
        for j in range(9):
            collst.append(lst[j][i])
        if sorted(collst) == [1,2,3,4,5,6,7,8,9]:
            cnt += 1
    if cnt == 9:
        return True

def block(lst):
    cnt=0
    for i in [2, 5, 8]:
        for j in [2,5,8]:
            smallblock = [lst[i-2][j-2], lst[i-2][j-1], lst[i-2][j], lst[i-1][j-2], lst[i-1][j-1],lst[i-1][j], lst[i][j-2],lst[i][j-1],lst[i][j]]
            if sorted(smallblock) == [1,2,3,4,5,6,7,8,9]:
                cnt += 1
    if cnt == 9:
        return True

def check(lst):
    if row(lst) and col(lst) and block(lst):
        return '1'
    else:
        return '0'

T = int(input())
result = ''
for z in range(T):
    board =[]
    for i in range(9):
        line = list(map(int, input().split()))
        board.append(line)
    a = check(board)
    result = result+ a

for z in range(T):
    print(f'#{z+1} {result[z]}')