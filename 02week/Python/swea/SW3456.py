# 직사각형의 네 변 중에서 세 변의 길이가 주어진다.

# 나머지 한 변의 길이가 얼마인지 출력하는 프로그램을 작성하라.

# 세 변의 길이는 상하좌우 어디든 될 수 있으므로 그 순서는 중요하지 않다.

# 입력으로 직사각형이 불가능한 경우는 주어지지 않는다.


# 다음 그림의 예시는 각각 a = 4, b = 3, c = 4의 입력과 a = 5, b = 5, c = 5의 입력을 받았을 때 직사각형의 모습이다.

# 빨간 숫자로 표시된 나머지 변의 길이를 출력하면 된다.

T = int(input())
for z in range(T):
    a, b, c = map(int,input().split())
    if a == b and b == c and c == a: # 정사각형
        print(f'#{z+1} {a}') 
    elif a==b and a !=c: # 직사각형
        print(f'#{z+1} {c}')
    elif a==c and a != b:
        print(f'#{z+1} {b}')
    else:
        print(f'#{z+1} {a}')