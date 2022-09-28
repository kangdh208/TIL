# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 시간초과
while True:
    n = int(input())
    if n !=0:
        n2 = n*2
        cnt = 0
        for i in range(n+1, n2+1):
            if i ==1:
                continue
            for j in range(2, int(i**0.5)+1):
                if i%j == 0:
                    break
            else:
                cnt +=1
        print(cnt)
    else:
        break

# 새풀이
import sys

n_max = 123456
is_prime = [True] * (2 * n_max + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2, int((2 * n_max) ** 0.5) + 1):
    if is_prime[i]:
        j = 2
        while (i * j) <= (2 * n_max):
            is_prime[i * j] = False
            j += 1

while (n := int(sys.stdin.readline())) != 0:
    print(is_prime[n + 1:(2 * n) + 1].count(True))
