# 체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.



board = []
for _ in range(8):
    line= list(input())
    board.append(line)
cnt=0
for row in range(len(board)):
    for col in range(len(board[row])):
        if (row+col) %2 ==0 and board[row][col]=='F':
            cnt+=1
print(cnt)