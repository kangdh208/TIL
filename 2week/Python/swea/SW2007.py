# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.

T = int(input())
for z in range(T):
    string = input()
    for i in range(1, len(string)-1):
        if string[i] == string[0] and string[i+1] == string[1]:
            print(f'#{z+1} {i}')
            break