# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.

# 예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.

def mirror(letter): # 바꾸는 함수
    if letter == 'b':
        return 'd'
    elif letter == 'd':
        return 'b'
    elif letter == 'p':
        return 'q'
    else:
        return 'p'

T = int(input())
for z in range(T):
    string = input()
    gnirts = string[::-1] #뒤집고
    newstr =''
    for i in range(len(gnirts)):
        newstr += mirror(gnirts[i]) #뒤집어 더하기
    print(f'#{z+1} {newstr}')