# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 시간초과

def check(num):
    for i in range(2, num):
        if num%i ==0:
            return False
    return True

n = int(input())
prime = []
if check(n) == True:
    prime.append(n)
else:
    for i in range(2, n):
        if check(i)==True:
            while n%i == 0:
                n = n//i
                prime.append(i)
        else:
            i+=1
for i in range(len(prime)):
    print(prime[i])

# 새풀이

N = int(input())
m = 2
while N!=1:
    if N%m==0: 
        print(m) 
        N = N//m
    else:
        m += 1