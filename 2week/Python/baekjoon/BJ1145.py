# 다섯 개의 자연수가 있다. 이 수의 적어도 대부분의 배수는 위의 수 중 적어도 세 개로 나누어 지는 가장 작은 자연수이다.

# 서로 다른 다섯 개의 자연수가 주어질 때, 적어도 대부분의 배수를 출력하는 프로그램을 작성하시오.

lst = list(map(int, input().split()))
n = min(lst)
while True:
    cnt = 0
    for i in lst:
        if n%i == 0:
            cnt+=1
    if cnt>2:
        print(n)
        break
    n +=1
