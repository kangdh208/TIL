# 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

N = int(input())
result = []
for i in range(N):
    lst = list(map(int, input().split()))
    cnt = max(lst)
    result.append(cnt)

for i in range(N):
    print(f"#{i+1} {result[i]}")