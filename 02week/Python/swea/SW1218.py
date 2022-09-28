# 4 종류의 괄호문자들 '()', '[]', '{}', '<>' 로 이루어진 문자열이 주어진다.

# 이 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별하는 프로그램을 작성한다.

for z in range(10):
    a = int(input())
    line = input()
    stack = []
    lft = ['(','{','[','<']
    rgt = [')','}',']','>']
    for i in range(a):
        scnt = 0
        if line[i] in lft:
            stack.append(line[i])
        elif line[i] in rgt:
            if lft.index(stack[-1]) ==rgt.index(line[i]):
                stack.pop()
            else:
                break
    if len(stack) !=0:
        print(f'#{z+1} 0')
    else:
        print(f'#{z+1} 1')