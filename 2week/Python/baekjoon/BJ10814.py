# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

# 틀렸습니다
N = int(input())
dic = {}
for _ in range(N):
    age, name = input().split()
    dic[name] = age
member = dict(sorted(dic.items(), key=lambda x:x[1]))

for k, v in member.items():
    print(v, k)
# 긁풀
import sys
input = sys.stdin.readline
N = int(input())
user = []
for _ in range(N):
    user.append(list(input().split()))
user.sort(key = lambda x:int(x[0]))
for i in range(N):
    print(user[i][0], user[i][1])