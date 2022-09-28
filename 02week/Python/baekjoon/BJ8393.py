# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
sig = 0
i = 0
while i<=n:
    sig +=i
    i +=1
print(sig)