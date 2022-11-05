# 정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.

# A와 B는 양의 정수이고, A < B를 만족한다.
# A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
# 집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.

import sys

input = sys.stdin.readline
L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.sort()
if n in S:
    print(0)
else:
    start = 0
    end = 0
    for i in S:
        if i < n:
            start = i
        elif i > n and end == 0:
            end = i
    end -= 1
    start += 1
    print((n - start) * (end - n + 1) + (end - n))
