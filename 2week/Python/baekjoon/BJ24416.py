# 오늘도 서준이는 동적 프로그래밍 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# 오늘은 n의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다. 재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자. 아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

# 피보나치 수 재귀호출 의사 코드는 다음과 같다.
# fib(n) {
#     if (n = 1 or n = 2)
#     then return 1;  # 코드1
#     else return (fib(n - 1) + fib(n - 2));
# }
# 피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

# fibonacci(n) {
#     f[1] <- f[2] <- 1;
#     for i <- 3 to n
#         f[i] <- f[i - 1] + f[i - 2];  # 코드2
#     return f[n];
# }

# 시간초과
def fib(n):
    global cnt1
    cnt1+=1
    if n == 1 or n==2:
        cnt1 -=1
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fibb(n):
    global cnt2
    f[1],f[2] = 1,1
    for i in range(3,n+1):
        cnt2+=1
        f[i] = f[i-1]+f[i-2]
    return f[n]

N = int(input())
f = [0 for _ in range(41)]
cnt1,cnt2 = 0,0
fib(N)
fibb(N)
print(cnt1 + 1, cnt2)

# 긁풀(시간초과)g-d
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
        
def fibonacci(n):
    dp=[0]*(n+1)
    dp[1],dp[2]=1,1
    cnt2=0
    for i in range(3,n+1):
        cnt2+=1
        dp[i]=dp[i-1]+dp[i-2]
    return cnt2

n=int(input())
print(fib(n),fibonacci(n))