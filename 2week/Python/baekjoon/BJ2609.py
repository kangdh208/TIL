# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

A,B = map(int, input().split())
divisor = [] # 공약수 리스트
d_A = [] # A의 약수리스트
for d1 in range(1, A+1):
    if A % d1 == 0: #약수이면
        d_A.append(d1) #약수리스트에 추가
d_B = []
for d2 in range(1, B+1):
    if B % d2 ==0:
        d_B.append(d2)
for div in d_A:
    if div in d_B:
        divisor.append(div)
print(divisor[-1])
mul = 1
while mul*A % B != 0:
    mul += 1
print(mul*A)