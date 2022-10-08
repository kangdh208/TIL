# 현수는 학생들에게 노래를 가르치고 있다. 총 N개의 악보가 있고 i번째 악보는 Bi초로 이루어져 있다. 학생들은 0초부터 1번 악보를 따라 노래하기 시작했다. 즉 B1-1초에 1번 악보를 끝마치게 되고 B1초부터 B1+B2-1초까지 2번 악보를 따라 부르게 된다.
# 문제는 T1부터 TQ까지 Q개의 시간에 대해 대답을 하는 것인데, Ti초 때 노래하는 악보를 i번째에 출력하는 것이다.

import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
for _ in range(Q):
    q = int(input())
    for i in range(N):
        if q < sum(lst[: i + 1]):
            print(i + 1)
            break
