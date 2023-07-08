# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

N = int(input())
number = [] * N
for _ in range(N):
    x, y = map(int, input().split())
    number.append([y, x])
num = sorted(number)
for i in range(len(num)):
    print(num[i][1], num[i][0])

# 새풀
N = int(input())
number = []
for _ in range(N):
    number.append([map(int, input().split())])
number.sort(key=lambda x: (x[1], x[0]))
for i in number:
    print(i[0], i[1])
