# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.

N = int(input())
result = []
for i in range(N):
    cnt = 0
    lst = list(map(int, input().split()))
    for j in lst:
        if j %2 != 0:
            cnt += j
    result.append(cnt)

for i in range(N):
    print(f"#{i+1} {result[i]}")