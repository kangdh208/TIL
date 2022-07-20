# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

n =int(input())
q = []
r =[]
for i in range(0, n):
    a, b = map(int, input().split())
    q.append(a//b)
    r.append(a%b)
for i in range(0, n):
    print(f"#{i+1} {q[i]} {r[i]}")
