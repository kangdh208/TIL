# 이 문제는 아주 평범한 배낭에 관한 문제이다.

# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

import sys, pprint

input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0, 0]]  # 물건 가치 리스트
lst = [[0] * (K + 1) for i in range(N + 1)]
for _ in range(N):
    stuff.append(list(map(int, input().split())))
print(stuff)
print(lst)

for i in range(1, N + 1):
    for j in range(1, K + 1):  # 물건 가치 추가
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:  # 추가시 무게가 넘치면 추가 포기
            lst[i][j] = lst[i - 1][j]
            print(lst)
        else:  # 넣을 수 있으면 가치가 큰거
            lst[i][j] = max(lst[i - 1][j], lst[i - 1][j - weight] + value)
print(lst[N][K])  # 출력

# 내 지금 배낭에 새로운 애를 넣을 수 있는지


# 긁풀
# n, k = map(int, read().split())
# tmplst = [0] * (k+1)

# for _ in range(n):
#     w, v = map(int, read().split())
#     for j in range(k, w-1, -1):
#         tmplst[j] = max(tmplst[j], tmplst[j-w] + v)
# print(tmplst[-1])


# 새풀
# import sys

# input = sys.stdin.readline

# N, K = list(map(int, input().split()))

# lst = []
# for _ in range(N):
#     lst.append(list(map(int, input().split())))
# li = sorted(lst, key=lambda x: (x[0], -x[1]))

# # 물건 줍는다 -> 현재 가방 무게(temp)에 물건 무게 더한것이 한도 무게(K) 보다 적다면 다음물건으로 진행
# temp = 0  # 현재가방무게

# happiness_ans = 0

# for j in range(len(li)):
#     weight = 0
#     happiness = 0
#     for i in range(len(li)):  # 첫시작하는 물건의 무게가 li[j][0]부터 시작하도록 해야함 근데 현재는 li[i][0]부터 시작함
#         if i >= j:
#             if weight + li[i][0] <= K:
#                 weight += li[i][0]
#                 happiness += li[i][1]
#                 if happiness_ans < happiness:
#                     happiness_ans = happiness
#             else:
#                 break

# print(happiness_ans)
