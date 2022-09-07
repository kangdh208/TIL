# 상근이는 트럭을 총 세 대 가지고 있다. 오늘은 트럭을 주차하는데 비용이 얼마나 필요한지 알아보려고 한다.

# 상근이가 이용하는 주차장은 주차하는 트럭의 수에 따라서 주차 요금을 할인해 준다.

# 트럭을 한 대 주차할 때는 1분에 한 대당 A원을 내야 한다. 두 대를 주차할 때는 1분에 한 대당 B원, 세 대를 주차할 때는 1분에 한 대당 C원을 내야 한다.

# A, B, C가 주어지고, 상근이의 트럭이 주차장에 주차된 시간이 주어졌을 때, 주차 요금으로 얼마를 내야 하는지 구하는 프로그램을 작성하시오.

a, b, c = map(int, input().split())
park = [0]*100
for _ in range(3):
    intro, outro = map(int, input().split())
    for i in range(intro, outro):
        park[i] += 1
fee = 0
for i in range(len(park)):
    if park[i]==1:
        fee += a
    elif park[i]==2:
        fee += 2*b
    elif park[i]==3:
        fee += 3*c
print(fee)