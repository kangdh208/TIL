# 문빙이는 새해를 좋아한다. 하지만, 이제 새해는 너무 많이 남았다. 그래도 문빙이는 새해를 기다릴 것이다.

# 어느 날 문빙이는 잠에서 깨면서 스스로에게 물었다. “잠깐, 새해가 얼마나 남은거지?”

# 이 문제에 답하기 위해서 문빙이는 간단한 어플리케이션을 만들기로 했다. 연도 진행바라는 것인데, 이번 해가 얼마나 지났는지를 보여주는 것이다.

# 오늘 날짜가 주어진다. 이번 해가 몇%지났는지 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

mon, day, year, time = input().split()

Month = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
monthly = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mon = Month.index(mon) + 1
day = int(day[0:2])
year = int(year)
hour = int(time[0:2])
minute = int(time[3:5])
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    monthly[1] += 1
total = sum(monthly) * 24 * 60
today = (sum(monthly[:mon]) + day - 1) * 24 * 60 + hour * 60 + mon
print(today / total * 100)


# 긁풀
Month, D, Y, T = input().split()
D = int(D[:-1])
Y = int(Y)
H, M = map(int, T.split(":"))
month_name_li = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
month_day_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0):
    month_day_li[1] += 1
total_time = sum(month_day_li) * 24 * 60

last_month_idx = month_name_li.index(Month)
current_time = (sum(month_day_li[:last_month_idx]) + D - 1) * 24 * 60 + H * 60 + M
print(current_time / total_time * 100)
