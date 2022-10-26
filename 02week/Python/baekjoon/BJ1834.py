# N으로 나누었을 때 나머지와 몫이 같은 모든 자연수의 합을 구하는 프로그램을 작성하시오. 예를 들어 N=3일 때, 나머지와 몫이 모두 같은 자연수는 4와 8 두 개가 있으므로, 그 합은 12이다.

import sys

input = int(sys.stdin.readline())

N = input
remain = [i for i in range(1, N)]
number = 0
for i in remain:
    number += i * N + i
print(number)
