# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
N = int(input())
t = []
for i in range(N):
    a, b = map(int, input().split())
    if a>b:
        t.append('>')
    elif a<b:
        t.append('<')
    else:
        t.append('=')
for i in range(N):
    print(f'#{i+1} {t[i]}')