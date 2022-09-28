# 자연수 N와 R가 주어진다. 이 때의 N combination R의 값을 1234567891로 나눈 나머지를  출력하세요.

# 예를들면 N이 4, R이 2라면 4 combination 2는 (4 * 3) / (2 * 1) = 6이 된다.

try:
    while True:
        tc = int(input())
        n, r = map(int, input().split())
        fr = 1
        en = 1
        for i in range(r):
            num = n-i
            fr *= num
        for i in range(1,r+1):
            en *= i
        com = int(fr/en)
        remain = int(com%1234567891)
        print(f'#{tc} {remain}')
except:
    exit()