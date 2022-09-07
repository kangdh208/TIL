# 지난주에, 민식주식회사는 IIHF(International Ice Hockey Federation)로부터 긴급한 전화를 받았다.

# IIHF는 같은 팀이 링크안에 너무 많으면 알람이 울리는 시스템을 설치해달라고 요청했다. 시스템은 다음과 같이 3개의 부분으로 이루어진다.

# 디지털카메라가 링크의 사진을 매 1초마다 찍는다.
# 디지털카메라가 찍은 사진에서 각 선수의 위치를 뽑아낸다.
# 하키 링크 안에 같은 팀 선수가 총 몇 명인지 계산한다.
# 하키 링크는 (X, Y)가 가장 왼쪽 아래 모서리인 W * H 크기의 직사각형과, 반지름이 H/2이면서 중심이 (X, Y+R), (X+W, Y+R)에 있는 두 개의 원으로 이루어져 있다. 아래 그림을 참고한다.

# 선수들의 위치가 주어질 때, 링크 안 또는 경계에 있는 선수가 총 몇 명인지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
W,H,X,Y,P = map(int, input().split())
cnt = 0
for _ in range(P):
    x,y = map(int,input().split())
    if X<=x<=X+W and Y<=y<=Y+H:
        cnt += 1
    elif ((x-X)**2 + (y-(Y+(H/2)))**2)**0.5<=(H/2) or ((x-(X+W))**2 + (y-(Y+(H/2)))**2)**0.5<=(H/2):
        cnt +=1
print(cnt)