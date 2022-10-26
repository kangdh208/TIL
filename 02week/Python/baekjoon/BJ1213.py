# 임한수와 임문빈은 서로 사랑하는 사이이다.

# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.

# 임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

# from collections import deque
# import sys

# input = sys.stdin.readline

# word = sorted(list(input()))
# lst = deque()
# queue = deque(word)
# queue.popleft()
# if len(queue) % 2 == 0:
#     a = queue.popleft()
#     b = queue.popleft()
#     if a == b:
#         lst.appendleft(a)
#         lst.append(b)
#     else:
#         print("I'm sorry")
#         break
# else:
#     if len(queue) % 2 != 1:
#         while len(queue)
#             a = queue.popleft()
#             b = queue.popleft()
#             if a == b:
#                 lst.appendleft(a)
#                 lst.append(b)
#             else:
#                 print("I'm sorry")
#     else:
#         lst.append(queue[0])

import sys
from collections import Counter

word = list(map(str, sys.stdin.readline().strip()))
word.sort() # 사전순으로 정렬하기 위해 오름차순 정렬
check = Counter(word) # 홀수의 개수를 확인하기 위해 Counter 함수 사용

cnt = 0 # 홀수의 개수
center = "" # 홀수의 문자

# 반복문을 통해 각 문자의 개수를 확인
for i in check:
    # 문자의 개수가 홀수일 경우
    # 홀수의 개수를 카운트하고 홀수의 문자를 더해준다.
    if check[i] % 2 != 0:
        cnt += 1
        center += i
        word.remove(i) # 홀수의 문자 하나를 문자열에서 제거

    # 홀수의 개수가 1보다 클 경우 팰린드롬으로 바꾸지 못한다.
    if cnt > 1:
        break

# 홀수의 개수가 1보다 클 경우 팰린드롬으로 바꾸지 못한다.
if cnt > 1:
    print("I'm Sorry Hansoo")

# 홀수의 개수가 1 이하일 경우에는 팰린드롬으로 바꿀 수 있다.
else:

    res = ""
    # 반복문을 통해 팰린드롬을 반을 나누었을 때 왼쪽 부분을 더해준다.
    for i in range(0, len(word), 2):
        res += word[i]

    # 왼쪽 + 가운데(홀수) + 오른쪽
    print(res + center + res[::-1])