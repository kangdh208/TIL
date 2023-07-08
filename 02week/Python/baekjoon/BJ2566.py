# 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

lst = []
for _ in range(9):
    lst.append(list(map(int, input().split())))
x, y = 1, 1
maxNum = lst[0][0]
for i in range(9):
    for j in range(9):
        if maxNum < lst[i][j]:
            maxNum = lst[i][j]
            x, y = i + 1, j + 1
print(maxNum)
print(x, y)
