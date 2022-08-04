# N개의 정수가 입력으로 주어진다.

# 이때 연속하여 몇 개의 정수를 골라 합을 구할 수 있다.

# 예를 들어, 1 3 -8 18 -8 이 있다고 하자.

# 그럼 2번부터 4번까지의 수를 골라 합을 구하면, 3+(-8)+18 = 13이다. 

# 이렇게 연속해서 정수를 골라 합을 구할 때, 그 합의 최대가 몇인지 구하는 프로그램을 작성하세요.


#어디가틀렸지??
T = int(input())
for z in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    maxlst = []
    for i in range(N-1):
        numsum = lst[i]
        for j in range(i+1, N):
            numsum += lst[j]
            if numsum < numsum -lst[j]:
                numsum = numsum-lst[j]
                break
        maxlst.append(numsum)
    maxlst.append(lst[-1])    
    print(f'#{z+1} {max(maxlst)}')

# 긁어온 풀이
T = int(input())
for TC in range(1, T+1):
    N = int(input())
    Arr = list(map(int, input().split()))
    # 최대값 초기화
    maxV = -1000000
    # 합 초기화
    sumV = 0
    # 시작 인덱스 탐색
    for i in range(N):
        # 처음부터 더하기
        sumV += Arr[i]
        # 최대값 갱신
        if sumV > maxV:
            maxV = sumV
        # 현재까지의 합이 음수이면 버리기
        if sumV < 0:
            sumV = 0
    print("#{} {}".format(TC, maxV))