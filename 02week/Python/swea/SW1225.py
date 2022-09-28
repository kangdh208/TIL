# 다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

# - 8개의 숫자를 입력 받는다.

# - 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 

# 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

# 이와 같은 작업을 한 사이클이라 한다.

# - 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.


# recursion error
def cycle(lst):
    for i in range(1,6):
        if lst[0]-i>0:
            lst.append(lst[0]-i)
            lst.pop(0)
        else:
            lst.append(0)
            lst.pop(0)
            lst = map(str,lst)
            return lst
    return cycle(lst)

for i in range(10):
    num = int(input())
    old = list(map(int,input().split()))
    pwd = cycle(old)
    print(f'#{num} {" ".join(pwd)}')

# New Sol
while True:
    try:
        num = int(input())
        pwd = list(map(int, input().split()))
        i= 1
        while True:
            if i>5:
                i=1
            chk = pwd.pop(0)-i
            if chk>0:
                pwd.append(chk)
            else:
                pwd.append(0)
                break
            i += 1
        pwd = map(str, pwd)
        newnum = ' '.join(pwd)
        print(f'#{num} {newnum}')
    except EOFError:
        break