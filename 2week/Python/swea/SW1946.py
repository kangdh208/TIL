# 원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다.

# 문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.

# 이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다. (예 : A 5    AAAAA)

# 압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.

T = int(input())
for z in range(T):
    N = int(input())
    string = ''
    for y in range(N):
        a, b = input().split()
        string += a*int(b)
    print(f'#{z+1}')
    for i in range(len(string)):
        if (i+1)%10 == 0:
            print(string[i])
        else:
            print(string[i], end='')
    print()
