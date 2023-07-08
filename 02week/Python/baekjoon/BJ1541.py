# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

# line = input().split("-")
# num = []
# for i in line:
#     cnt = 0
#     cut = i.split("+")
#     for j in cut:
#         cnt += int(j)
#     num.append(cnt)
# n = num[0]
# for i in range(1, len(num)):
#     n -= num[i]
# print(n)

# import sys

# input = sys.stdin.readline

# result = 0

# x = list(input().strip().split("-"))

# for i in x:
#     num = i.split("+")
#     i = 0
#     tmp = 0
#     for j in num:
#         tmp += int(j)
#     i = tmp
# print(x)
# n = int(x[0])
# for i in range(1, len(x)):
#     n -= int(x[i])
# print(n)


# import sys

# input = sys.stdin.readline

# result = 0

# x = list(input().strip().split("-"))
# numlst = []
# for i in x:
#     num = i.split("+")
#     tmp = 0
#     for j in num:
#         tmp += int(j)
#     numlst.append(tmp)
# n = int(numlst[0])
# for i in range(1, len(numlst)):
#     n -= int(numlst[i])
# print(n)


def plus(string):
    if string.find('+') == -1:
        return int(string)
    else:
        lst = string.split("+")  # 플러스 기준 쪼개고
        num = int(lst[0])  # 처음값 설정하고
        for i in range(1, len(lst)):
            num += int(lst[i])  # 각각 더하기
        return num


line = input().strip()  # 문자열 받고
idx = line.find("-")  # - 위치찾고
num = 0  # 결과값 변수 선언
if idx == -1:  # 마이너스가 없으면
    if line.find('+') == -1:
        num = int(line)
    else:
        num = plus(line)
else:  # - 있으면
    number1 = line[:idx]  # - 앞
    number2 = line[idx + 1 :]  # - 뒤
    num1 = plus(number1)  # 앞부분 + 더하기
    num2 = plus(number2)  # 뒤부분 + 더하고
    num = num1 - num2  # 앞부분 - 뒤부분
print(int(num))  # 출력
