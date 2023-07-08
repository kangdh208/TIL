# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.


# def avg(lst, num):  # 산술평균
#     ans = int(sum(lst) / num)
#     return ans


# def mid(lst, num):  # 중앙값
#     lst = sorted(lst)
#     ans = lst[int((num - 1) / 2)]
#     return ans


# def mode(lst, num):  # 최빈값
#     counts = dict()
#     for i in range(1, num + 1):
#         counts[i] = []
#     maxcnt = 1
#     cnt = 1
#     for j in range(1, num):
#         if lst[j] == lst[j - 1]:
#             cnt += 1
#         else:
#             counts[cnt].append(lst[j - 1])
#             if maxcnt < cnt:
#                 maxcnt = cnt
#             cnt = 1
#         if j == num - 1:
#             counts[cnt].append(lst[j])
#             if maxcnt < cnt:
#                 maxcnt = cnt

#     if num == 1:
#         counts[1].append(lst[0])

#     counts[maxcnt].sort()
#     if len(counts[maxcnt]) == 1:
#         return counts[maxcnt][0]
#     else:
#         return counts[maxcnt][1]


# def ran(lst):  # 범위
#     m = max(lst)
#     n = min(lst)
#     return m - n


# number = []
# numb = int(input())
# for _ in range(numb):
#     number.append(int(input()))

# print(avg(number, numb))
# print(mid(number, numb))
# print(mode(number, numb))
# print(ran(number))

# 카운터풀이

from collections import Counter
import sys

input = sys.stdin.readline
numbers = []
for _ in range(int(input())):
    num = int(input())
    numbers.append(num)

numbers.sort()

cnt = Counter(numbers).most_common(2)

print(round(sum(numbers) / len(numbers)))  # 산술평균
print(numbers[len(numbers) // 2])  # 중앙값
if len(numbers) > 1:  # 최빈값
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(numbers) - min(numbers))  # 범위

# 시간 초과 > pypy3
def func(lst, num):
    numberCount = dict()
    for i in range(N):
        if lst[i] not in numberCount:
            numberCount[lst[i]] = 1
        else:
            numberCount[lst[i]] += 1
    max_value = max(numberCount.values())
    maxNumber = []
    for i in numberCount.keys():
        if numberCount[i] == max_value:
            maxNumber.append(i)
    if len(maxNumber) == 1:
        return maxNumber[0]
    else:
        return maxNumber[1]


N = int(input())
number = []
for _ in range(N):
    number.append(int(input()))
number.sort()

# 산술평균
print(int(round(sum(number) / N)))
# 중앙값
print(number[int((N - 1) / 2)])
# 최빈값
print(func(number, N))
# 범위
print(number[-1] - number[0])
