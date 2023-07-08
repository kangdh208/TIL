# 도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

# 도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
house = []
for _ in range(N):  # 1. 집 리스트 만들고 정렬
    house.append(int(input()))
house.sort()
start, end = 1, house[-1] - house[0]  # 2. 집들 사이 거리 초기화 : 최소 1, 최대 끝집-첫집
result = 0
while start <= end:  # 3. 집들 사이 거리 기준 이분 탐색
    mid = (start + end) // 2
    cnt = 1
    location = house[0]
    # 현재 탐색하는 집의 위치와 직전에 설치했던 집의 위치가
    # middle 보다 크거나 같을 때는 공유기 댓수 추가
    # 마지막 설치 위치 갱신
    for i in range(N):
        if house[i] - location >= mid:
            cnt += 1
            location = house[i]
    # middle 거리에 설치 가능 댓수가 K에 미달시 거리 좁힘
    if cnt >= K:  # 4. 거리 중 최댓값 갱신
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1
print(result)


import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()
answer = 0

start, end = 1, house[-1] - house[0]
while start <= end:
    middle = (start + end) // 2
    cnt = 1  # 공유기 숫자
    location = house[0]  # 현재 위치
    for i in range(N):
        if house[i] - location >= middle:
            cnt += 1
            location = house[i]
    if cnt >= C:
        answer = max(middle, answer)
        start = middle + 1
    else:
        end = middle - 1
print(answer)
