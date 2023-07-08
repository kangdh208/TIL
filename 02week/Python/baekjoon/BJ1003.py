# 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }
# fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# import sys

# input = sys.stdin.readline

# T = int(input())
# fibo = [0, 1, 1]
# for i in range(3, 41):
#     number = fibo[i - 1] + fibo[i - 2]
#     fibo.append(number)
# for _ in range(T):
#     N = int(input())
#     if N == 0:
#         print(1, 0)
#     elif N == 1:
#         print(0, 1)
#     else:
#         print(fibo[N - 1], fibo[N])


import sys

input = sys.stdin.readline

T = int(input())

fibo = [0, 1, 1]
for i in range(3, 41):
    fibo.append(fibo[i - 1] + fibo[i - 2])
for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(fibo[N - 1], fibo[N])
