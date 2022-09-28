# 영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다. 예를 들어, 긴 글에서 약 12.31% 글자는 e이다.

# 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.read



line = input().replace('\n','').replace(' ','')
alpha = [0] * 26
for i in line:
    alpha[ord(i)-97]+=1
maxnumb = max(alpha)
maxlist = []
for i in range(len(alpha)):
    if alpha[i] == maxnumb:
        maxlist.append(chr(i+97))
maxlist.sort()
print(*maxlist,sep='')