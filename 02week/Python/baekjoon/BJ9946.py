# 준하는 유치원에서 단어 퍼즐게임을 즐겨한다.

# 단어 퍼즐게임이란, 주어진 알파벳들을 섞어서 단어를 만드는 게임이다.

# 천재 준하는 알파벳을 임의로 조합하여, 사전과 매칭된 단어를 만드는 프로그램을 만들어 단어를 완성시켰다.

# 그러나 완성된 단어를 원장님에게 가져가려는 순간, 지나가던 강민이와 부딫혀서 단어조각을 땅에 떨어뜨리고 말았다.

# 준하는 어찌어찌 조각을 회수했지만, 순서는 뒤죽박죽이 되었고, 알파벳이 부족하거나 다른 알파벳이 섞였을 수도 있다.

# 준하가 처음에 완성한 단어와 나중에 회수한 알파벳들이 주어질 때,

# 준하가 알파벳을 제대로 회수했는지 안했는지 판단하는 프로그램을 만들어주자.

import sys

input = sys.stdin.readline
cnt = 1
while True:
    junha = input()
    puzzle = input()
    if puzzle == "END\n":
        break
    else:
        if sorted(list(junha)) == sorted(list(puzzle)):
            print(f"Case {cnt}: same")
            cnt += 1
        else:
            print(f"Case {cnt}: different")
            cnt += 1
