# 농부 민식이가 관리하는 농장은 N×M 격자로 이루어져 있다. 민식이는 농장을 관리하기 위해 산봉우리마다 경비원를 배치하려 한다. 이를 위해 농장에 산봉우리가 총 몇 개 있는지를 세는 것이 문제다.

# 산봉우리의 정의는 다음과 같다. 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어져 있다. (여기서 "인접하다"의 정의는 X좌표 차이와 Y좌표 차이 모두 1 이하일 경우로 정의된다.) 또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.

# 문제는 격자 내에 산봉우리의 개수가 총 몇 개인지 구하는 것이다.


from pprint import pprint


n, m = map(int, input().split())
zerolist = []
for i in range(m+2):
    zerolist.append(0)
farm = []
farm.append(zerolist)
zero = [0]
for z in range(n):
    line =(list(map(int,input().split())))
    line = zero + line + zero
    farm.append(line)
farm.append(zerolist)
# pprint(farm)
cnt=0
for i in range(1, n+1):
    for j in range(1, m+1):
        if farm[i][j] >= max(farm[i-1][j-1],farm[i-1][j],farm[i-1][j+1],farm[i][j-1],farm[i][j+1],farm[i+1][j-1],farm[i+1][j],farm[i+1][j+1]):
            cnt +=1
            print((i,j))
        if farm[i][j] == max(farm[i-1][j-1],farm[i-1][j],farm[i-1][j+1],farm[i][j-1],farm[i][j+1],farm[i+1][j-1],farm[i+1][j],farm[i+1][j+1]):
            cnt-=1
            print(f"- {(i,j)}")
print(cnt)
