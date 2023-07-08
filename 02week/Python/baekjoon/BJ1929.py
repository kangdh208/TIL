# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 시간초과
# def check(num):
#     for i in range(2, num):
#         if num%i ==0:
#             return False
#     return True

# M,N = map(int, input().split())
# for i in range(M,N+1):
#     if check(i) == True:
#         print(i)

# # 새풀이
# M,N = map(int, input().split())
# for i in range(M, N+1):
#     if i ==1:
#         continue
#     for j in range(2, int(i**0.5)+1):
#         if i%j == 0:
#             break
#     else:
#         print(i)


def check(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


import sys

input = sys.stdin.readline
M, N = map(int, input().split())
for i in range(M, N+1):
    if check(i) == True:
        print(i)
