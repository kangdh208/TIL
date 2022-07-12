# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# sum() 함수 사용 금지
n1 = int(input())
sum1 = n1
while n1>0:
    n1 = n1-1
    sum1 += n1
print(sum1)

n2 = int(input())
sum2 = 0
for i in range(0, n2+1):
    sum2 +=i
print(sum2)