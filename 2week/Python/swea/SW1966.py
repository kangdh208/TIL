# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.

T = int(input())
for z in range(T):
    n = int(input())
    numbers = list(map (int,input().split()))
    number = sorted(numbers)
    for i in range(n):
        number[i] = str(number[i])
    number = " ".join(number)
    print(f'#{z+1} {number}')