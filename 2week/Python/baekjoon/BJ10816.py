# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

N = int(input())
have = list(map(int, input().split()))
havelst ={}
for i in range(len(have)):
    if have[i] in havelst:
        havelst[have[i]] += 1
    else:
        havelst[have[i]] = 1
M = int(input())
check = list(map(int, input().split()))
checklst =[]
for i in check:
    if i in havelst:
        checklst.append(str(havelst[i]))
    else:
        checklst.append('0')
print(" ".join(checklst))