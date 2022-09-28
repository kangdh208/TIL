# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

# ***
# * *
# ***

# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

N=int(input())
def starpick(num):
    if num==1:
        return ['*']
    stars=starpick(num//3)
    Line=[]
    for i in stars:
        Line.append(i*3)
    for i in stars:
        Line.append(i+' '*(num//3)+i)
    for i in stars:
        Line.append(i*3)
    return Line

print('\n'.join(starpick(N)))
