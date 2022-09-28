# 월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.

# 리스트로 풀면 한케이스 틀림????
T = int(input())
for z in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    differ = m2 - m1
    day1 = 0
    if m2-m1>=2:
        if m1==1 or m1==3 or m1==5 or m1==7 or m1==8 or m1==10 or m1==12:
            day1 = 31-d1
        elif m1 ==2:
            day1 = 28-d1
        else:
            day1 = 30 -d1
    day2 = 0
    for y in range(1, differ):
        y=m1 +y
        if y > 12:
            y = y-12
        if y==1 or y==3 or y==5 or y==7 or y==8 or y==10 or y==12:
            day2 += 31
        elif y ==2:
            day2 += 28
        else:
            day2 += 30
    day3 = d2 +1
    
    day = day1+day2+day3
    print(f'#{z+1} {day}')

# 딕셔너리 접근법
T = int(input())
for z in range(T):
    m1, d1, m2, d2 = map(int, input().split())
    calender = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    result = 0
    for i in range(m1, m2):
        if m1 == i:
            result += calender[i]-d1 +1
        else:
            result += calender[i]
    result += d2
    print(f'#{z+1} {result}')