# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.


# 왜틀렸지??
def check(num):
    for i in range(2, num):
        if num %i ==0:
            return False
    return True

M = int(input())
N = int(input())
primesum = 0
prime = []
for i in range(M, N+1):
    if check(i) == True:
        prime.append(i)
        primesum += i
if len(prime) >=1:
    print(primesum)
    print(prime[0])
else:
    print(-1)

# New Way

M = int(input())
N = int(input())
prime = []
for i in range(M, N+1):
    if i == 1:
        pass
    elif i == 2:
        prime.append(i)
    else:
        for j in range(2, i):
            if i%j ==0:
                break
            elif j == i-1:
                prime.append(i)
if len(prime)>0:
    print(sum(prime))
    print(min(prime))
else:
    print('-1')