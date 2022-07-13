# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지
numbers =map(int, input().split())
number = list(numbers)
minnum = number[0]
for i in range(1, len(number)):
    if minnum >= number[i]:
        minnum = number[i]

print(minnum)