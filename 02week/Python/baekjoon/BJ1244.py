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

# 긁풀
def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N+1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N//2):
            if num + k > N or num - k < 1 : break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break
                
for i in range(1, N+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()