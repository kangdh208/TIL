# 임한수와 임문빈은 서로 사랑하는 사이이다.

# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.

# 임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.

# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

from collections import deque
import sys

input = sys.stdin.readline

word = sorted(list(input()))
lst = deque()
queue = deque(word)
queue.popleft()
print(queue)
if len(queue) % 2 == 0:
    a = queue.popleft()
    b = queue.popleft()
    if a == b:
        lst.appendleft(a)
        lst.append(b)
    else:
        print("I'm sorry")
else:
    if len(queue) % 2 != 1:
        a = queue.popleft()
        b = queue.popleft()
        if a == b:
            lst.appendleft(a)
            lst.append(b)
        else:
            print("I'm sorry")
    else:
        lst.append(queue[0])
