# 민석이는 교수가 되었고, 이번에 처음으로 맡은 과목에 수강생이 N명이다.

# 민석이는 처음으로 과제를 내었다.

# 그리고 제출한 사람의 목록을 받았다.

# 수강생들은 1번에서 N번까지 번호가 매겨져 있고, 어떤 번호의 사람이 제출했는지에 대한 목록을 받은 것이다.

# 과제를 제출하지 않은 사람의 번호를 오름차순으로 출력하는 프로그램을 작성하라.

T = int(input())
for z in range(T):
    st, hw = map(int, input().split())
    lst = list(map(int, input().split()))
    std = []
    for i in range(1,st+1):
        if i not in lst:
            std.append(str(i))
    answer = ' '.join(std)
    print(f'#{z+1} {answer}')