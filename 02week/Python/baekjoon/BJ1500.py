# 세준이는 정수 S와 K가 주어졌을 때, 합이 S인 K개의 양의 정수를 찾으려고 한다. 만약 여러개일 경우 그 곱을 가능한 최대로 하려고 한다.

# 가능한 최대의 곱을 출력한다.

# 만약 S=10, K=3이면, 3,3,4는 곱이 36으로 최대이다.

import sys

S, K = map(int, sys.stdin.readline().split())
Q = S // K
R = S % K
N = 1
while K > 0:
    if R > 0:
        N *= Q + 1
        R -= 1
    else:
        N *= Q
    K -= 1
print(N)
