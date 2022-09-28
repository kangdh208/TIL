# 어린 왕자는 소혹성 B-664에서 자신이 사랑하는 한 송이 장미를 위해 살아간다. 어느 날 장미가 위험에 빠지게 된 것을 알게 된 어린 왕자는, 장미를 구하기 위해 은하수를 따라 긴 여행을 하기 시작했다. 하지만 어린 왕자의 우주선은 그렇게 좋지 않아서 행성계 간의 이동을 최대한 피해서 여행해야 한다.
# 은하수 지도, 출발점, 도착점이 주어졌을 때 어린 왕자에게 필요한 최소의 행성계 진입/이탈 횟수를 구하는 프로그램을 작성해 보자. 행성계의 경계가 맞닿거나 서로 교차하는 경우는 없다. 또한, 출발점이나 도착점이 행성계 경계에 걸쳐진 경우 역시 입력으로 주어지지 않는다.

import sys 
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sx,sy,ex,ey = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int,input().split())
        d1 = (sx-cx)**2 + (sy-cy)**2
        d2 = (ex-cx)**2 + (ey-cy)**2
        if r**2>d1 and r**2 >d2:
            pass
        elif r**2>d1:
            cnt+=1
        elif r**2>d2:
            cnt+=1
    print(cnt)