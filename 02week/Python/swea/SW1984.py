# 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.

# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

T = int(input())
for z in range(1, T+1):
    numbers = list(map(int, input().split()))
    maxnum = max(numbers)
    minnum = min(numbers)
    avg = round((sum(numbers)-maxnum-minnum)/8)
    print(f'#{z} {avg}')