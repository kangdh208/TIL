# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline
lst_i = []
lst_j = []
while True:
    a, b= map(int, input().split())
    if a != 0 and b != 0:
        lst_i.append(a)
        lst_j.append(b)
    else:
        break
n = len(lst_i)
for i in range(0, n):
    adding = lst_i[i] + lst_j[i]
    print(adding)