# 카드를 퍼펙트 셔플 한다는 것은, 카드 덱을 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미한다. 

# N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.

# 만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.
from collections import deque

T = int(input())
for z in range(T):
    N = int(input())
    if N %2 == 0:
        mid = int(N/2)
        deck = list(input().split())
        Front = deque(deck[:mid])
        End = deque(deck[mid:])
        new = []
        while len(Front)!=0 and len(End)!=0:
            new.append(Front[0])
            Front.popleft()
            new.append(End[0])
            End.popleft()
        line = ' '.join(new)
        print(f'#{z+1} {line}')
    else:
        mid = int(N//2+1)
        deck = list(input().split())
        Front = deque(deck[:mid])
        End = deque(deck[mid:])
        new = []
        while len(Front)!=0 and len(End)!=0:
            new.append(Front[0])
            Front.popleft()
            new.append(End[0])
            End.popleft()
        new.append(deck[mid-1])
        line = ' '.join(new)
        print(f'#{z+1} {line}')
