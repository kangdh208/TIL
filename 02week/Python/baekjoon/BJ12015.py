# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# bisect 안쓴 풀이
import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
lst = [0]
for i in seq:
    if lst[-1] < i:
        lst.append(i)
    else:
        start, end = 0, len(lst)
        while start <= end:
            middle = (start + end) // 2
            if lst[middle] < i:
                start = middle + 1
            else:
                end = middle - 1
        lst[start] = i
        print(i, start, "istart")
print(len(lst) - 1)

# bisect 사용 풀이
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
ㅇ
N = int(input())
seq = list(map(int, input().split()))
lst = [0]
for i in seq:
    if lst[-1] < i:
        lst.append(i)
    else:
        startidx = bisect_left(lst, i)
        lst[startidx] = i
        print(i, startidx, "istart")
print(len(lst) - 1)
