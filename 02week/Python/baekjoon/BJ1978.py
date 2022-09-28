# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 런타임 에러
def check(num):
    cnt =0
    result = 0
    if num >1:
        for i in range(2, num+1):
            if num % i ==0:
                cnt += 1
            else:
                cnt +=1
        if cnt == num -1:
            result = 1
    return result


N = int(input())
lst = list(map(int, input().split()))
primecnt = 0
for i in range(len(lst)):
    j = check(lst[i])
    if j ==1:
        primecnt +=1
print(primecnt)

numbers = list(map(int, input().split()))

# 새방법
n = int(input())
numbers = map(int, input().split())
prime = 0
for num in numbers:
    notprime = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                notprime += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if notprime == 0:
            prime += 1  # error가 없으면 소수.
print(prime)