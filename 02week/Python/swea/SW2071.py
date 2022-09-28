# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

N = int(input())
numlst = []
for i in range(0,N):
    n = list(map(int, input().split()))
    result = sum(n)
    avg = int(round(result/10))
    numlst.append(avg)
for i in range(N):
    print(f'#{i+1} {numlst[i]}')