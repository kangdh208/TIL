# n choose m의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline
# 시간초과
n, m = map(int, input().split())
com = 1
for i in range(m):
    mul = n-i
    com *=mul
div =1
for j in range(1,m+1):
    div *=j
combi=str(int(com/div))[::-1]
cnt = 0
for i in combi:
    if i == '0':
        cnt+=1
    else:
        break
print(cnt)
#시간초과
n, m = map(int, input().split())
com = 1
for i in range(m):
    mul = n-i
    com *=mul
div =1
for j in range(1,m+1):
    div *=j
combi=int(com/div)
cnt = 0
dcv = 1
for i in range(len(str(combi))):
    if combi%dcv == 0:
        dcv =10*(i+1)
        cnt+=1
    else:
        break
print(cnt-1)
# 긁풀
n, m = map(int, input().split())


def two_count(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two

def five_count(n):
    five = 0
    while n != 0:
        n = n // 5
        five += n
    return five

print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))