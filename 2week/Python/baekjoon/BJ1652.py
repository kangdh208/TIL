# 일 년 동안 세계일주를 하던 영식이는 여행을 하다 너무 피곤해서 근처에 있는 코레스코 콘도에서 하룻밤 잠을 자기로 하고 방을 잡았다.

# 코레스코 콘도에 있는 방은 NxN의 정사각형모양으로 생겼다. 방 안에는 옮길 수 없는 짐들이 이것저것 많이 있어서 영식이의 누울 자리를 차지하고 있었다. 영식이는 이 열악한 환경에서 누울 수 있는 자리를 찾아야 한다. 영식이가 누울 수 있는 자리에는 조건이 있다. 똑바로 연속해서 2칸 이상의 빈 칸이 존재하면 그 곳에 몸을 양 옆으로 쭉 뻗으면서 누울 수 있다. 가로로 누울 수도 있고 세로로 누울 수도 있다. 누울 때는 무조건 몸을 쭉 뻗기 때문에 반드시 벽이나 짐에 닿게 된다. (중간에 어정쩡하게 눕는 경우가 없다.)

# 방의 크기 N과 방의 구조가 주어졌을 때, 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 구하는 프로그램을 작성하시오.

N = int(input())
room = []
for _ in range(N):
    room.append(list(input()))

row = 0
col = 0
rcnt =0
ccnt =0
for i in room:
    for j in i:
        if i == '.':
            rcnt +=1
        else:
            if rcnt >=2:
                row += 1
            rcnt = 0
    if rcnt >= 2:
        row +=1
    rcnt = 0
for i in range(N):
    for j in range(N):
        if room[j][i] == '.':
            ccnt +=1
        else:
            if ccnt >=2:
                col +=1
            ccnt = 0
    if ccnt >= 2:
        col +=1
    ccnt = 0
print(row, col)