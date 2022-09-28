# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지
import math
#10진법 내풀이
n = int(input())
numdig = 1
decim = 10
while True:
    if 0<n<=9:
        break
    div = n/decim
    if div >= 10:
        decim *= 10
        numdig += 1
    else:
        numdig += 1
        break
print(numdig)
#로그풀이 # Math import 필수
m = int(input())
log = math.log10(m)
print(int(log)+1)
#수업풀이(10진법다른풀이) - 나눗셈접근
l = int(input())
cnt = 0
result =0 
while l != 0: #while number : #number ==0이면 False 니까.
    result //= 10
    cnt +=1
print(cnt)
