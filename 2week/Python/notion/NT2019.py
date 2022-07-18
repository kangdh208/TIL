# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

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