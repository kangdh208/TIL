# "럭키스톤"은 카드를 통해 대결하는 게임이다. 창식이는 럭키스톤을 자주 한다.

# 이 게임의 카드에는 공격력과 생명력이 표시되어있다. 왼쪽에는 공격력이, 오른쪽에는 생명력이 숫자로 적혀있다.

# 서로 꺼낸 카드를 비교하여 남길 카드를 결정하는 데, 카드의 비교는 다음과 같이 이루어진다.

# 비교하는 카드의 공격력만큼 동시에 서로 상대 카드의 생명력을 깎는다. 줄어든 생명력은 다시 회복되지 않는다.
# 생명력이 0 이하인 경우에는 카드는 죽은 상태로 전환된다.
# 카드가 두 장 모두 남아있다면 비교를 계속한다.
# 요즘 따라 게임이 안 풀리는 창식이는 대전 전에 가능한 수를 미리 계산하여 최대한 이득을 챙기고 싶어 한다.

# 카드 2개의 공격력과 생명력이 주어지면 어떤 플레이어의 카드가 남아있을지 출력하는 프로그램을 작성해주자.

import sys

input = sys.stdin.readline

# 외않되?
# def battle(A_a, B_a, A_l, B_l):
#     A_l -= B_a
#     B_l -= A_a
#     if A_l <= 0 and B_l <= 0:
#         print("DRAW")
#     elif A_l <= 0 and B_l > 0:
#         print("PLAYER B")
#     elif A_l > 0 and B_l <= 0:
#         print("PLAYER A")
#     elif A_l > 0 and B_l > 0:
#         battle(A_a, B_a, A_l, B_l)


# A_attack, A_life = map(int, input().split())
# B_attack, B_life = map(int, input().split())
# battle(A_attack, B_attack, A_life, A_life)

a1, h1 = map(int, input().split())
a2, h2 = map(int, input().split())
a, b = h1 // a2 + (1 if h1 % a2 else 0), h2 // a1 + (1 if h2 % a1 else 0)
if a == b:
    print("DRAW")
elif a > b:
    print("PLAYER A")
else:
    print("PLAYER B")
