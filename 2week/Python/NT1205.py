# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

numbers = (input().split())
string = numbers
count = 0
for i in string:
    count += 1
sum = 0
for i in range(0, count):
    numint = int(numbers[i])
    sum += numint
average = sum/count
print(average)