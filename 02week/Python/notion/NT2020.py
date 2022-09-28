# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

#내풀이
n = int(input())
dec = 10
lst = []
while True:
    if n != 0:
        rem = n % dec
        n = (n - rem)//10
        lst.append(rem)
    else:
        break
numsum = sum(lst)
print(numsum)
num = int(input())

#남풀이

# Algorithm - str()
num = str(num)
ans = 0
for i in num:
  ans += int(i)
print(ans)

# Algorithm - while loop
ans = 0

while num :
  x = num % 10
  ans += x
  num //= 10

print(ans)