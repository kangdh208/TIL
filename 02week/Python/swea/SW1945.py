# 숫자 N은 아래와 같다.

# N=2a x 3b x 5c x 7d x 11e

# N이 주어질 때 a, b, c, d, e 를 출력하라.

T = int(input())
result = []
for z in range(T):
    n = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    prime = [2,3,5,7,11]
    while n%2 ==0:
        n=n//2
        a+=1
    while n%3 ==0:
        n=n//3
        b+=1
    while n%5 ==0:
        n=n//5
        c+=1
    while n%7 ==0:
        n=n//7
        d+=1
    while n%11 ==0:
        n=n//11
        e+=1
    numbers = f'{a} {b} {c} {d} {e}'
    result.append(numbers)

for i in range(T):
    print(f'#{i+1} {result[i]}')