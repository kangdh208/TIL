# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

T = int(input())
for z in range(T):
    a, b = map(int, input().split())
    result = 0
    board = []
    for y in range(a):
        line = list(map(int, input().split()))
        board.append(line)
    ans = 0
    for x in range(a):
        cnt = 0
        for w in range(a):
            if (board[x][w] == 1):
                cnt+=1
                if cnt == b+1:
                    ans-=1
                elif cnt == b :
                    ans+=1
            else:
                cnt = 0
        cnt1 = ans
    ans = 0
    for x in range(a):
        cnt = 0
        for w in range(a):
            if (board[w][x] == 1):
                cnt+=1
                if cnt == b+1:
                    ans-=1
                elif cnt == b :
                    ans += 1
            else:
                cnt = 0
        cnt2 = ans
    tcnt = cnt1+cnt2
    print(f'#{z+1} {tcnt}')