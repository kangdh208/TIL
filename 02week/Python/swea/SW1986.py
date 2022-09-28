# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

N = int(input())
lst =[]
for i in range(0, N):
    n = int(input())
    sumall = 0
    for j in range(1, n+1):
        if j % 2 == 0:
            sumall -= j
        else:
            sumall += j
    lst.append(sumall)
for i in range(0,N):
    print(f'#{i+1} {lst[i]}')