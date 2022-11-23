import sys

input = sys.stdin.readline


def boy(lst, num):
    i = 1
    while num * i <= N:
        if lst[num * i - 1] == 1:
            lst[num * i - 1] = 0
        elif lst[num * i - 1] == 0:
            lst[num * i - 1] = 1
        i += 1
    return lst


def girl(lst, num):
    i = 1
    lft = num - 1
    rgt = num - 1
    while 0 <= lft and rgt < N:
        lft -= i
        rgt += i
        if lft != rgt:
            break
        if lst[lft] == lst[rgt]:
            if lst[lft] == 1:
                lst[lft] = 0
                lst[rgt] = 0
            elif lst[rgt] == 0:
                lst[lft] = 1
                lst[rgt] = 1
    return lst


N = int(input())
lst = list(map(int, input().split()))
student = int(input())
for i in range(student):
    gender, number = map(int, input().split())
    if gender == 1:
        lst = boy(lst, number)
        print(lst)
    elif gender == 2:
        lst = girl(lst, number)
        print(lst)
lst = map(str, lst)
print(" ".join(lst))
