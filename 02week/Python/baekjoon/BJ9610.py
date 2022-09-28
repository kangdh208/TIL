# 2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

N = int(input())
dic = {
    'Q1':0,
    'Q2':0,
    'Q3':0,
    'Q4':0,
    'AXIS':0
}
for i in range(N):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        dic['AXIS'] += 1
    elif x > 0 and y > 0:
        dic['Q1'] += 1
    elif x < 0 and y > 0:
        dic['Q2'] += 1
    elif x < 0 and y < 0:
        dic['Q3'] += 1
    elif x > 0 and y < 0:
        dic['Q4'] += 1
print('Q1:', dic['Q1'])
print('Q2:', dic['Q2'])
print('Q3:', dic['Q3'])
print('Q4:', dic['Q4'])
print('AXIS:', dic['AXIS'])