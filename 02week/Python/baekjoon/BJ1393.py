# 최백준은 음하철도 구구팔에 탔다.

# 문제는 구구팔의 기장인 조교 김재홍이 반쯤 미쳐서 열차를 멈추지 않는다는 것이다. 그래서 최백준은 달리고 있는 열차에서 뛰어내려야 한다.

# 그런데 뛰어내릴 때 정류장 까지 거리가 너무 멀면 마이 아플 수 있다.

# 그래서 철도가 정류장에 가장 많이 근접했을 때 뛰어내리고자 한다.

# 어디서 뛰어내려야 하는가?
def gcd(A, B):
    cnt = min(A, B)
    while True:
        if A % cnt == 0 and B % cnt == 0:
            return cnt
        else:
            cnt -= 1


XS, YS = map(int, input().split())
EX, EY, DX, DY = map(int, input().split())

d = gcd(DX, DY)
dx = DX // d
dy = DY // d
dist = (XS - EX) ** 2 + (YS - EY) ** 2
while True:
    EX += dx
    EY += dy
    if (XS - EX) ** 2 + (YS - EY) ** 2 >= dist:
        dist = (XS - EX) ** 2 + (YS - EY) ** 2
    else:
        print(EX, EY)
        break


# 긁풀
import sys
import math


def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def check_distance(x, y):
    return math.sqrt((x - xs) ** 2 + (y - ys) ** 2)


xs, ys = map(int, sys.stdin.readline().split())
xe, ye, dx, dy = map(int, sys.stdin.readline().split())

d_gcd = get_gcd(dx, dy)
dx, dy = dx // d_gcd, dy // d_gcd

curx, cury = xe, ye
while check_distance(curx, cury) > check_distance(curx + dx, cury + dy):
    curx += dx
    cury += dy

print(curx, cury)
