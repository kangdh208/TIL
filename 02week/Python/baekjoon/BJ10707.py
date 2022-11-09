# JOI군이 살고 있는 지역에는 X사와 Y사, 두 개의 수도회사가 있다. 두 회사의 수도요금은 한 달간 수도의 사용량에 따라 다음과 같이 정해진다.

# X사 : 1리터당 A엔.
# Y사 : 기본요금은 B엔이고, 사용량이 C리터 이하라면 요금은 기본요금만 청구된다. 사용량이 C리터가 넘었을 경우 기본요금 B엔에 더해서 추가요금이 붙는다. 추가요금은 사용량이 C리터를 넘었을 경우 1리터를 넘었을 때마다 D엔이다.
# JOI군의 집에서 한 달간 쓰는 수도의 양은 P리터이다.

# 수도요금이 최대한 싸게 되도록 수도회사를 고를 때, JOI군의 집의 1달간 수도요금을 구하여라.

import sys

input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
X = A * P
if C >= P:
    Y = B
elif C < P:
    Y = B + (P - C) * D
print(min(X, Y))
