# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

x = []
y = []
xy = []
for _ in range(3):
    X,Y=input().split()
    x.append(X)
    y.append(Y)
for i in range(3):
    if x.count(x[i]) == 1:
        xp = x[i]
    if y.count(y[i]) == 1:
        yp = y[i]
print(xp,yp)