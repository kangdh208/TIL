# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# import sys, heapq

# input = sys.stdin.readline
# # heap 사용
# N = int(input())
# heap = []
# for _ in range(N):
#     number = int(input())
#     if number == 0:
#         if len(heap) == 0:
#             print(0)
#         else:
#             print((-1) * heapq.heappop(heap))
#     else:
#         heapq.heappush(heap, -number)


# from math import *

# # 내가 만들래요


# def insert(heap, num):
#     heap.append(num)

#     i = len(heap) - 1
#     while i > 1:
#         if heap[i] > heap[i // 2]:
#             tmp = heap[i]
#             heap[i] = heap[i // 2]
#             heap[i // 2] = tmp
#             i = i // 2
#         else:
#             break


# def remove(heap):
#     maxheap = heap[1]
#     tmp = heap.pop()

#     upNode = 1
#     downNode = 2

#     while downNode <= len(heap) - 1:
#         if downNode < len(heap) - 1 and heap[downNode] < heap[downNode + 1]:
#             downNode += 1
#         if heap[downNode] <= tmp:
#             break
#         heap[upNode] = heap[downNode]
#         upNode = downNode
#         downNode *= 2

#     if len(heap) != 1:
#         heap[upNode] = tmp
#     return maxheap


# N = int(input())
# heap = [0]
# for _ in range(N):
#     num = int(input())
#     if num == 0:
#         if len(heap) == 1:
#             print(0)
#         else:
#             print(remove(heap))
#     else:
#         insert(heap, num)


# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import sys, heapq

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print((-1) * heapq.heappop(heap))
    else:
        heapq.heappush(heap, (-1) * x)
