# 매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.

# 예를 들어, 아래와 같이 10일 간의 온도가 주어졌을 때,

# 3 -2 -4 -9 0 3 7 13 8 -3

# 모든 연속적인 이틀간의 온도의 합은 아래와 같다.


# 이때, 온도의 합이 가장 큰 값은 21이다.

# 또 다른 예로 위와 같은 온도가 주어졌을 때, 모든 연속적인 5일 간의 온도의 합은 아래와 같으며,


# 이때, 온도의 합이 가장 큰 값은 31이다.

# 매일 측정한 온도가 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오.


import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

part_sum = sum(lst[:K])
result = [part_sum]

for i in range(0, len(lst) - K):
    part_sum = part_sum - lst[i] + lst[i + K]
    result.append(part_sum)

print(max(result))
