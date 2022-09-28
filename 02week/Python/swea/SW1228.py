# 0 ~ 999999 사이의 수를 나열하여 만든 암호문이 있다.

# 암호문을 급히 수정해야 할 일이 발생했는데, 이 암호문은 특수 제작된 처리기로만 수정이 가능하다.

# 이 처리기는 다음과 같이 1개의 기능을 제공한다.

# 1. I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]

# 위의 규칙에 맞게 작성된 명령어를 나열하여 만든 문자열이 주어졌을 때, 암호문을 수정하고, 수정된 결과의 처음 10개 숫자를 출력하는 프로그램을 작성하여라.

for z in range(10):
    A = int(input())
    B = list(map(int,input().split()))
    C = int(input())
    D = list(input().split('I '))
    D = D[1:]
    for i in range(len(D)): # 명령어 쪼개서 리스트화
        element = list(map(int, D[i].split()))
        NewD = []
        NewD.append(element)
        idx = NewD[0][0]
        if NewD[0][0]:
            B = B[:idx] + NewD[0][2 : 3+C] + B[idx:]
        else:
            B = NewD[0][2 : 3+C] + B
    password = []
    for i in range(10):
        password.append(str(B[i]))
    answer = ' '.join(password)
    print(f'#{z+1} {answer}')

