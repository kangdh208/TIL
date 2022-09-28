# 시골에 있는 태양이의 삼촌 댁에는 커다란 참외밭이 있다. 문득 태양이는 이 밭에서 자라는 참외가 도대체 몇 개나 되는지 궁금해졌다. 어떻게 알아낼 수 있는지 골똘히 생각하다가 드디어 좋은 아이디어가 떠올랐다. 유레카! 1m2의 넓이에 자라는 참외 개수를 헤아린 다음, 참외밭의 넓이를 구하면 비례식을 이용하여 참외의 총개수를 구할 수 있다.

# 1m2의 넓이에 자라는 참외의 개수는 헤아렸고, 이제 참외밭의 넓이만 구하면 된다. 참외밭은 ㄱ-자 모양이거나 ㄱ-자를 90도, 180도, 270도 회전한 모양(┏, ┗, ┛ 모양)의 육각형이다. 다행히도 밭의 경계(육각형의 변)는 모두 동서 방향이거나 남북 방향이었다. 밭의 한 모퉁이에서 출발하여 밭의 둘레를 돌면서 밭경계 길이를 모두 측정하였다.

# 1m2의 넓이에 자라는 참외의 개수와, 참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이가 순서대로 주어진다. 이 참외밭에서 자라는 참외의 수를 구하는 프로그램을 작성하시오.

# 틀렸습니다.
n = int(input())
field = [list(map(int, input().split())) for _ in range(6)]

width = 0
widthidx = 0
height = 0
heightidx = 0
for i in range(len(field)):
    if field[i][0] == 1 or field[i][0] == 2: # 방향이 동서면 가로
        if width  < field[i][1]:
            width = field[i][1]
            widthidx = i
    elif field[i][0] == 3 or field[i][0] == 4: # 방향이 남북은 세로
        if height<field[i][1]:
            height = field[i][1]
            heightidx = i
    widthsmall = abs(field[(widthidx-1)%6][1] - field[(widthidx+1)%6][1])
    heightsmall = abs(field[(heightidx-1)%6][1] - field[(heightidx+1)%6][1])
    result = ((width*height)-(widthsmall*heightsmall))*n
    print(result)

# 새풀이
import sys

K = int(sys.stdin.readline())

#E=1, W=2, S=3, N=4
height = []
width = []
total = []
#동서쪽으로 움직이는 경우와 남북쪽으로 움직이는 경우를 나눠서 리스트에 넣어준다.
for i in range(6):
    dir, length = map(int, sys.stdin.readline().split())
    if dir == 1 or dir ==2:
        width.append(length)
        total.append(length)
    else:
        height.append(length)
        total.append(length)

bigbox = max(height) * max(width)

#세로 최대값 
maxhidx = total.index(max(height))
#가로최대값 
maxwidx = total.index(max(width))

#전체 이동에서 세로 최대값의 다음값에서 세로 최대값 이전의 가로값을 빼준것이 작은 사각형의 가로값 
small1 = abs(total[maxhidx-1] - total[(maxhidx-5 if maxhidx == 5 else maxhidx +1)])

small2 = abs(total[maxwidx-1] - total[(maxwidx-5 if maxwidx == 5 else maxwidx +1)])
area = bigbox - (small1 * small2)
print(area*K)