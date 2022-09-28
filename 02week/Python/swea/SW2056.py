# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면

# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,

# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.


# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
# 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
N = int(input())
result = []
month1 = ['01','03','05','07','08','10','12',]
month2 = ['04','06','09','11']
month3 = ['02']
for i in range(N):
    ymd = input()
    y = ymd[:4]
    m = ymd[4:6]
    d = ymd[6:]
    if y != '0000':
        if m in month1:
            if int(d) in range(1, 32):
                result.append(f'{y}/{m}/{d}')
            else:
                result.append('-1')
        elif m in month2:
            if int(d) in range(1, 31):
                result.append(f'{y}/{m}/{d}')
            else:
                result.append('-1')
        elif m in month3:
            if int(d) in range(1, 29):
                result.append(f'{y}/{m}/{d}')
            else:
                result.append('-1')
        else:
            result.append('-1')
for i in range(N):
    print(f'#{i+1} {result[i]}')