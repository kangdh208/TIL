# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

numbers =map(int, input().split())
number = list(numbers)
maxnum = number[0]
for i in range(1, len(number)):
    if maxnum <= number[i]:
        maxnum = number[i]

print(maxnum)