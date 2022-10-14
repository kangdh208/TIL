# 정래는 김밥가게 “그르다 김가놈”에 납품할 김밥을 만드는 김밥 공장을 운영한다. 정래는 김밥 양쪽 끝을 “꼬다리”라고 부른다. 그리고 꼬다리를 잘라낸 김밥을 “손질된 김밥”이라고 부른다.

# 공장에서는 김밥 N개에 대해서, 김밥 꼬다리를 잘라내고 손질된 김밥을 김밥조각으로 만드는 작업을 한다. 꼬다리를 잘라낼 때에는 양쪽에서 균일하게 K cm만큼 잘라낸다. 만약 김밥의 길이가 2K cm보다 짧아서 한쪽밖에 자르지 못한다면, 한쪽만 꼬다리를 잘라낸다. 김밥 길이가 K cm이거나 그보다 짧으면 그 김밥은 폐기한다.

# 손질된 김밥들은 모두 일정한 길이 P로 잘라서 P cm의 김밥조각들로 만든다. P는 양의 정수여야 한다. 정래는 일정한 길이 P cm로 자른 김밥조각을 최소 M개 만들고 싶다. P를 최대한 길게 하고 싶을 때, P는 얼마로 설정해야 하는지 구하시오.

import sys

input = sys.stdin.readline

N, K, M = map(int, input().split())
lst = []
for _ in range(N):
    line = int(input())
    if line <= K:
        line = 0
    elif K < line <= (2 * K):
        line -= K
    elif line > (2 * K):
        line -= 2 * K
    lst.append(line)
maxcut = max(lst)
cntlst = []
for i in range(1, maxcut):
    cnt = 0
    for j in range(N):
        cnt += lst[j] // i
    if cnt >= M:
        cntlst.append(i)
if len(cntlst) == 0:
    print(-1)
else:
    print(max(cntlst))

# pypy3 제출 필수
