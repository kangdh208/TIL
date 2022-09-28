# N x N 행렬이 주어질 때, 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

T = int(input())
for z in range(T):
    N = int(input())
    case=[]
    
    for y in range(N):
        lninpt = list(input().split())
        line = list(''.join(lninpt))
        case.append(line)
    print(f'#{z+1}')
    for x in range(N):
        a =''
        for w in range(N):
            a += case[N-1-w][x]
        b = ''
        for w in range(N):
            b += case[N-1-x][N-1-w]
        c = ''
        for w in range(N):
            c += case[w][N-1-x]
        print(a, b, c)