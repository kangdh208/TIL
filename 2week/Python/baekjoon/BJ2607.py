# 영문 알파벳 대문자로 이루어진 두 단어가 다음의 두 가지 조건을 만족하면 같은 구성을 갖는다고 말한다.

# 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
# 같은 문자는 같은 개수 만큼 있다.
# 예를 들어 "DOG"와 "GOD"은 둘 다 'D', 'G', 'O' 세 종류의 문자로 이루어져 있으며 양쪽 모두 'D', 'G', 'O' 가 하나씩 있으므로 이 둘은 같은 구성을 갖는다. 하지만 "GOD"과 "GOOD"의 경우 "GOD"에는 'O'가 하나, "GOOD"에는 'O'가 두 개 있으므로 이 둘은 다른 구성을 갖는다.

# 두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어라고 한다.

# 예를 들어 "DOG"와 "GOD"은 같은 구성을 가지므로 이 둘은 비슷한 단어이다. 또한 "GOD"에서 'O'를 하나 추가하면 "GOOD" 과 같은 구성을 갖게 되므로 이 둘 또한 비슷한 단어이다. 하지만 "DOG"에서 하나의 문자를 더하거나, 빼거나, 바꾸어도 "DOLL"과 같은 구성이 되지는 않으므로 "DOG"과 "DOLL"은 비슷한 단어가 아니다.

# 입력으로 여러 개의 서로 다른 단어가 주어질 때, 첫 번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n = int(input())
words = [[0 for _ in range(26)] for _ in range(n)]
for i in range(n):
    string = input().rstrip()
    for j in string:
        words[i][ord(j)-65] += 1
res = 0
for word in words[1:]:
    pl, mi = 0,0
    for i in range(26):
        if word[i] > words[0][i]:
            pl += (word[i]-words[0][i])
        else:
            mi += (words[0][i]-word[i])
    if pl < 2 and mi < 2:
        res += 1
print(res)