# 세준이는 N개의 빨대를 가지고 있다. N개의 빨대 중에 3개의 빨대를 선택했을 때, 이 빨대로 삼각형을 만들 수 있다면, 세 변의 길이의 합의 최댓값을 구하고 싶다.
import sys

input = sys.stdin.readline
N = int(input())
lst = list()
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
chk = False
for i in range(len(lst) - 2):
    if lst[i] < lst[i + 1] + lst[i + 2]:
        print(lst[i] + lst[i + 1] + lst[i + 2])
        chk = True
        break
if chk == False:
    print(-1)
