# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

N = int(input())
lst = []
for _ in range(N):
    lst.append(list((map(int, input().split()))))
num = sorted(lst)
for i in range(len(num)):
    loc = map(str,num[i])
    a = ' '.join(loc)
    print(a)