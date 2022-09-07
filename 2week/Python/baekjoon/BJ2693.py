# 배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성하시오.

# 배열 A의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.

T = int(input())
arr = []
for _ in range(T):
    line=list(map(int, input().split()))
    for i in range(2):
        maxnum = max(line)
        minnum = min(line)
        for i in range(len(line)):
            if line[i]==maxnum:
                line[i] = minnum
    print(max(line))