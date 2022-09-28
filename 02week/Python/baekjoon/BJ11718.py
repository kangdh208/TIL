# 입력 받은 대로 출력하는 프로그램을 작성하시오.

while True:
    try:
        print(input())
    except EOFError:
        break