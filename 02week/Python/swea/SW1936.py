# A와 B가 가위바위보를 하였다.

# 가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.

# A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

a, b = map(int,input().split())
if (a==1 and b ==2) or (a==2 and b==3) or (a==3 and b==1):
    print('B')
else:
    print('A')