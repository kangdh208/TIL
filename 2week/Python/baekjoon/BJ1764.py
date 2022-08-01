# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

N, M = map(int, input().split())
hear = {}
see = {}
for i in range(N):
    hearname = input()
    hear[hearname] = 'hear'
for i in range(M):
    seename = input()
    see[seename] = 'see'
hearsee = []
for k, v in hear.items():
    if k in see.keys():
        hearsee.append(k)
lst = sorted(hearsee)
print(len(lst))
for i in range(len(hearsee)):
    print(lst[i])