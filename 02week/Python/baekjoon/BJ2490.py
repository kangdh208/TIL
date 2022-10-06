# 우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다. 네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.

import sys

input = sys.stdin.readline


def chk(lst):
    cnt = 0
    for i in lst:
        if i == 1:
            cnt += 1
    if cnt == 0:
        answer = "D"
    elif cnt == 1:
        answer = "C"
    elif cnt == 2:
        answer = "B"
    elif cnt == 3:
        answer = "A"
    else:
        answer = "E"
    return answer


A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
print(chk(A))
print(chk(B))
print(chk(C))
