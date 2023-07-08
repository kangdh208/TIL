# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

import sys


def fact(n):
    if n == 1:
        return 1
    else:
        return n * (fact(n - 1))


N = int(sys.stdin.readline())
if N == 0:
    print(1)
else:
    print(fact(N))
