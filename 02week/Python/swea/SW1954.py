# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

T = int(input())
# 이동벡터 > 상우하좌
row_vector = [0,1,0,-1]
col_vector = [1,0,-1,0]

for z in range(T):
    n = int(input())
    snail = []
    for y in range(n):
        snail.append([0]*n)
    row, col = 0,0 # 시작하곳
    vector = 0 # 이동벡터 인덱스값 ()
    
    for i in range(1,n**2+1):
        snail[row][col] = i
        row += row_vector[vector]
        col += col_vector[vector]
        # 막혔어?
        if row<0 or col<0 or row>=n or col>=n or snail[row][col] != 0:
            row -= row_vector[vector] # 정지 정지
            col -= col_vector[vector] # 뒤로1보

            vector = (vector + 1) % 4 #인덱스 0123으로 초기화
            row += row_vector[vector] #내가 멈춘 이유는
            col += col_vector[vector] #전진하기 위해서
    
    print(f'#{z+1}')
    for i in range(len(snail)):
        a = snail[i]
        row_snail = ' '.join(map(str,snail[i]))
        print(row_snail)
