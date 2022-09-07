# 총 N개의 문자열로 이루어진 집합 S가 주어진다.

# 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

N, M = map(int,input().split())
S = []
T = []
for z in range(N):
    S.append(input())
for z in range(M):
    T.append(input())
# 풀이1
cnt=0
for i in T:
    if i in S:
        cnt +=1
print(cnt)

# 풀이2
print(len(set(S)&set(T)))