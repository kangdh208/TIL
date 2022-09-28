# 마라토너라면 국적과 나이를 불문하고 누구나 참가하고 싶어하는 백준 마라톤 대회가 열린다. 42.195km를 달리는 이 마라톤은 모두가 참가하고 싶어했던 만큼 매년 모두가 완주해왔다. 단, 한 명만 빼고! 

# 모두가 참가하고 싶어서 안달인데 이런 백준 마라톤 대회에 참가해 놓고 완주하지 못한 배부른 참가자 한 명은 누굴까?

#시간초과
N = int(input())
runner = {}
for i in range(N):
    run = input()
    if run in runner:
        runner[run] += 1
    else:
        runner[run] =1
for i in range(N-1):
    runner[input()] -= 1
for k, v in runner.items():
    if v ==1 :
        print(k)
        break

#구글링풀이
import sys 
input = sys.stdin.readline().rsrip()

start = dict()
finish = dict()

n = int(input())
for _ in range(n):
    name = input()
    if name in start:
        start[name] += 1
    else:
        start[name] = 1

for _ in range(n-1):
    name = input()
    if name in finish:
        finish[name] += 1
    else:
        finish[name] = 1

for n in start.keys():
    if n not in finish:
        print(n)
        break
    else:
        if start[n] != finish[n]:
            print(n)
            break