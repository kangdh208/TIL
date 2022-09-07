# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

# 틀렸습니다
N = int(input())
dic = {}
for _ in range(N):
    word = input()
    if word not in dic:
        dic[word] = len(word)
number = dict(sorted(dic.items(), key=lambda x:x[1]))
# print(number)
for k, v in number.items():
    print(k)

# 긁풀
import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)