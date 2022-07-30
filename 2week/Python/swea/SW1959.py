# N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.

# Ai 나 Bj 를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있다.

# 단, 더 긴 쪽의 양끝을 벗어나서는 안 된다.
# 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

T = int(input())
for z in range(T):
    I,J = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    differ = abs(I-J)
    calculate = []
    if I<J:
        for j in range(differ+1):
            cal=0
            for i in range(len(A)):
                cal += A[i]*B[i+j]
            calculate.append(cal)
    elif I>J:
        for j in range(differ+1):
            cal=0
            for i in range(len(B)):
                cal += A[i+j]*B[i]
            calculate.append(cal)
    else:
        cal = 0
        for i in range(len(A)):
            cal += A[i]*B[i]
        calculate.append(cal)
    print(f"#{z+1} {max(calculate)}")