# 주어진 숫자부터 0까지 순서대로 찍어보세요

n = int(input())
numlst = []
for i in range(0, n+1):
    numlst.append(str(n-i))
print(' '.join(numlst))
