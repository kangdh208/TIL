# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
# 시간초과
n = int(input())
com = 1
for i in range(1,n+1):
    com *=i
combi=str(com)[::-1]
cnt = 0
for i in combi:
    if i == '0':
        cnt+=1
    else:
        break
print(cnt)

# 긁풀
N = int(input())
print(N//5 + N//25 + N//125)