# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
N = int(input())

check_list = [0] * 10001

for i in range(N):
    input_num = int(input())
    check_list[input_num] = check_list[input_num] + 1
    
for i in range(10001):
    if check_list[i] != 0:
        for j in range(check_list[i]):
            print(i)