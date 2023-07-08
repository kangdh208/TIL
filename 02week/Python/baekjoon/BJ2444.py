# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

N = int(input())
for i in range(N):
    blank = " " * (N - 1 - i)
    star = "*" * (2 * i + 1)
    print(blank + star)
for i in range(1, N):
    j = N - i
    blank = " " * i
    star = "*" * (2 * j - 1)
    print(blank + star)
