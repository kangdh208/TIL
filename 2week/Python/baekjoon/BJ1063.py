# 8*8크기의 체스판에 왕이 하나 있다. 킹의 현재 위치가 주어진다. 체스판에서 말의 위치는 다음과 같이 주어진다. 알파벳 하나와 숫자 하나로 이루어져 있는데, 알파벳은 열을 상징하고, 숫자는 행을 상징한다. 열은 가장 왼쪽 열이 A이고, 가장 오른쪽 열이 H까지 이고, 행은 가장 아래가 1이고 가장 위가 8이다. 예를 들어, 왼쪽 아래 코너는 A1이고, 그 오른쪽 칸은 B1이다.

# 킹은 다음과 같이 움직일 수 있다.

# R : 한 칸 오른쪽으로
# L : 한 칸 왼쪽으로
# B : 한 칸 아래로
# T : 한 칸 위로
# RT : 오른쪽 위 대각선으로
# LT : 왼쪽 위 대각선으로
# RB : 오른쪽 아래 대각선으로
# LB : 왼쪽 아래 대각선으로
# 체스판에는 돌이 하나 있는데, 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 

# 입력으로 킹이 어떻게 움직여야 하는지 주어진다. 입력으로 주어진 대로 움직여서 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.

# 킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.

delta = {
    'R':(0,1),
    'L':(0,-1),
    'B':(1,0),
    'T':(-1,0),
    'RT':(-1,1),
    'LT':(-1,-1),
    'RB':(1,1),
    'LB':(1,-1)
}
king,stone,number = input().split()
ku, kv = 8-int(king[1]),ord(king[0])-65
su, sv = 8-int(stone[1]), ord(stone[0])-65
print(ku, kv, su, sv)
for _ in range(int(number)):
    go = input()
    x = delta[go][0]
    y = delta[go][1]
    ku +=x
    kv +=y
    su +=x
    su +=y
    if ku<0 or ku>7 or kv<0 or kv>7:
        ku-=x
        kv-=y
        print(ku,kv)
    if su<0 or su>7 or sv<0 or sv>7:
        su -=x
        sv -=y
        print(su,sv)
    if ku == su and kv == sv:
        ku -=x
        kv -=y
        su -=x
        sv -=y
        print('!')
king = chr(kv+65) + str(8-ku)
stone = chr(sv+65) + str(8-su)
print(king)
print(stone)

# 긁풀-런타임에러
def Move(split,key,flag,name):
    if key =='R' and ord(split[0]) <72:
        split[0]=chr(ord(split[0]) +1)
    elif key=="L" and ord(split[0]) >65:
        split [0]=chr(ord(split[0])-1)
    elif key=="B" and int(split[1]) > 1:
        split[1] = str(int (split [1])-1)
    elif key=='T' and int(split[1]) <8:
        split[1] = str((split[1])+1)
    elif key=="RT" and ord(split[0]) <72 and int(split[1]) < 8:
        split[0]=chr(ord(split[0]) +1)
        split[1] = str(int(split[1])+1)
    elif key=="LT" and ord(split[0]) >65 and int(split[1]) < 8:
        split [0] = chr(ord(split[0])-1) 
        split[1] = str(int(split[1])+1)
    elif key == "RB" and ord(split[0]) <72 and int(split[1]) > 15:
        split[0]=chr(ord(split[0]) +1)
        split[1]=str(int(split[1])-1)
    elif key=="LB" and ord(split[0]) >65 and int(split[1]) > 1:
        split[0] =chr(ord(split[0]) -1)
        split[1] =str(int(split[1])-1)
    else:
        if name=="stone":
            flag=1

    return split, flag

king,stone, n=input().split()
king_split=list(king)
stone_split=list(stone)
for _ in range(int (n)):
    key=(input())
    flag=0
    temp_k=[king_split[0].king_split[1]]
    temp_s=[stone_split[0],stone_split[1]]
    king_split, flag=Move(king_split,key,flag,"king")
    if "".join(king_split)==''.join(stone_split):
        stone_split,flag=Move(stone_split,key,flag,"stone")
        if flag == 1:
            king_split=temp_k
            stone_split=temp_s

# print("join(king split), join(stone_split))

print(''.join(king_split)) 
print(''.join(stone_split))
# 긁풀- 신박한 풀이
import sys
k, s, n = input().split()
move = [sys.stdin.readline().strip() for _ in range(int(n))]
row = ['A','B','C','D','E','F','G','H']
column = ['1','2','3','4','5','6','7','8']
king_idx = []
stone_idx = []
for i,p in enumerate(row):
    if p == k[0]:
        king_idx.append(i)
        break
for i,p in enumerate(column):
    if p == k[1]:
        king_idx.append(i)
        break
for i,p in enumerate(row):
    if p == s[0]:
        stone_idx.append(i)
        break
for i,p in enumerate(column):
    if p == s[1]:
        stone_idx.append(i)
        break

# 명령 수행
for i in move:
    if i == 'R':
        if king_idx[0] == 7:
            continue
        king_idx[0] += 1
        if king_idx == stone_idx:
            if stone_idx[0] == 7:
                king_idx[0] -= 1
                continue
            stone_idx[0] += 1
    elif i == 'L':
        if king_idx[0] == 0:
            continue
        king_idx[0] -= 1
        if king_idx == stone_idx:
            if stone_idx[0] == 0:
                king_idx[0] += 1
                continue
            stone_idx[0] -= 1
    elif i == 'B':
        if king_idx[1] == 0:
            continue
        king_idx[1] -= 1
        if king_idx == stone_idx:
            if stone_idx[1] == 0:
                king_idx[1] += 1
                continue
            stone_idx[1] -= 1
    elif i == 'T':
        if king_idx[1] == 7:
            continue
        king_idx[1] += 1
        if king_idx == stone_idx:
            if stone_idx[1] == 7:
                king_idx[1] -= 1
                continue
            stone_idx[1] += 1
    elif i == 'RT':
        if king_idx[1] == 7 or king_idx[0] == 7:
            continue
        king_idx[0] += 1
        king_idx[1] += 1
        if king_idx == stone_idx:
            if stone_idx[1] == 7 or stone_idx[0] == 7:
                king_idx[0] -= 1
                king_idx[1] -= 1
                continue
            stone_idx[0] += 1
            stone_idx[1] += 1
    elif i == 'LT':
        if king_idx[1] == 7 or king_idx[0] == 0:
            continue
        king_idx[0] -= 1
        king_idx[1] += 1
        if king_idx == stone_idx:
            if stone_idx[1] == 7 or stone_idx[0] == 0:
                king_idx[0] += 1
                king_idx[1] -= 1
                continue
            stone_idx[0] -= 1
            stone_idx[1] += 1
    elif i == 'RB':
        if king_idx[1] == 0 or king_idx[0] == 7:
            continue
        king_idx[0] += 1
        king_idx[1] -= 1
        if king_idx == stone_idx:
            if stone_idx[1] == 0 or stone_idx[0] == 7:
                king_idx[0] -= 1
                king_idx[1] += 1
                continue
            stone_idx[0] += 1
            stone_idx[1] -= 1
    elif i == 'LB':
        if king_idx[1] == 0 or king_idx[0] == 0:
            continue
        king_idx[0] -= 1
        king_idx[1] -= 1
        if king_idx == stone_idx:
            if stone_idx[1] == 0 or stone_idx[0] == 0:
                king_idx[0] += 1
                king_idx[1] += 1
                continue
            stone_idx[0] -= 1
            stone_idx[1] -= 1
print(row[king_idx[0]]+column[king_idx[1]])
print(row[stone_idx[0]]+column[stone_idx[1]])