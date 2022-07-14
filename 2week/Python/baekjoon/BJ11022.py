# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline
n = int(input())
lst_i = []
lst_j = []
m = 0
while m < n:
    a, b= map(int, input().split())
    lst_i.append(a)
    lst_j.append(b)
    m += 1
for i in range(0, n):
    adding = lst_i[i] + lst_j[i]
    print(f"Case #{i+1}: {lst_i[i]} + {lst_j[i]} = {adding}")