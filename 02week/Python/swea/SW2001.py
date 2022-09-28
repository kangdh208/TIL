# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

# 죽은 파리의 개수를 구하라!

T = int(input())
for z in range(T):
    N,M=map(int,input().split())
    board = []
    for y in range(N):
        line = list(map(int, input().split()))
        board.append(line)
    fly = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            catch = 0
            for c in range(M):
                for d in range(M):
                    if i + c in range(N) and j + d in range(N):
                        catch += board[i + c][j + d]
            fly.append(catch)
    print(f'#{z+1} {max(fly)}') 