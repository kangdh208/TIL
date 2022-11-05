# 히스토그램은 데이터를 시각적으로 표현한 것이다. 막대로 구성되며 각 막대의 길이는 데이터 양의 크기를 나타낸다. 일부 데이터가 주어지면 히스토그램을 생성하시오.

import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num = int(input())
    line = ["=" for _ in range(num)]
    print("".join(line))
