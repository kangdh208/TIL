# 예를 들어, 위와 같은 경우를 살펴보자. 이 경우, 기차 안에 사람이 가장 많은 때는 2번역에서 3명의 사람이 기차에서 내리고, 13명의 사람이 기차에 탔을 때로, 총 42명의 사람이 기차 안에 있다.

# 이 기차는 다음 조건을 만족하면서 운행된다고 가정한다.

# 기차는 역 번호 순서대로 운행한다.
# 출발역에서 내린 사람 수와 종착역에서 탄 사람 수는 0이다.
# 각 역에서 현재 기차에 있는 사람보다 더 많은 사람이 내리는 경우는 없다.
# 기차의 정원은 최대 10,000명이고, 정원을 초과하여 타는 경우는 없다.
# 4개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline
current_maximum = 0
cnt = 0
for _ in range(4):
    off, on = map(int, input().split())
    cnt -= off
    cnt += on
    if current_maximum <= cnt:
        current_maximum = cnt
print(current_maximum)
