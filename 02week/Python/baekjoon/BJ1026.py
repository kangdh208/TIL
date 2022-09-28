# 옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

# 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

# S = A[0] × B[0] + ... + A[N-1] × B[N-1]

# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.

# S의 최솟값을 출력하는 프로그램을 작성하시오.

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())),reverse=True)
S = 0
for i in range(N):
    S += A[i] * B[i]
print(S)