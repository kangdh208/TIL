# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
n1 = int(input())
mul1 = 1
while n1 > 0:
    mul1 *= n1
    n1 = n1-1
print(mul1)

n2 = int(input())
mul2 = 1
for i in range(1, n2+1):
    mul2 *= i
print(mul2)