# 영식이가 운동을 하는 과정은 1분 단위로 나누어져 있다. 매 분마다 영식이는 운동과 휴식 중 하나를 선택해야 한다.


# 영식이의 초기 맥박은 m이다. 운동을 N분 하려고 한다. 이때 운동을 N분하는데 필요한 시간의 최솟값을 구해보자. 운동하는 시간은 연속되지 않아도 된다.

import sys

input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())
beat = m
cnt = 0
time = 0
if m + T > M:
    print(-1)
else:
    while True:
        if beat + T >= M:
            beat = beat - R
            time += 1
        elif beat - R < m:
            beat = beat + T
            cnt += 1
            time += 1
        else:
            beat = beat + T
            cnt += 1
            time += 1
        if cnt == N:
            break
    print(time)

import sys

input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())
Time = 0
exercise = 0
heart_beat = m

if m + T > M:
    print(-1)
else:
    while exercise < N:
        if heart_beat + T <= M:
            heart_beat += T
            Time += 1
            exercise += 1
        else:
            heart_beat = max(heart_beat - R, m)
            Time += 1
    print(Time)
