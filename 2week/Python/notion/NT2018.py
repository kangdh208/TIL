# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

a = input()
dic = {}
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
for alpha, cont in dic.items():
    print(alpha, cont)

#수업풀이
b = input()
res = {}
for i in b:
    if not i in b:
        res[i] = 1
    else:
        res[i] = res[i] +1
for k in res:
    print(k, res[k])

#get 사용
c = input()
re = {}
for i in c:
    re[i] = re.get(i, 0) + 1
for k in re:
    print(k, re[k])