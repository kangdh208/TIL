# 한상덕은 이번에 중덕 고등학교에 새로 부임한 교장 선생님이다. 교장 선생님으로서 첫 번째 일은 각 반의 수학 시험 성적의 통계를 내는 일이다.

# 중덕 고등학교 각 반의 학생들의 수학 시험 성적이 주어졌을 때, 최대 점수, 최소 점수, 점수 차이를 구하는 프로그램을 작성하시오.

K = int(input())
for z in range(K):
    lst = list(map(int, input().split()))
    student = lst[0]
    lst.pop(0)
    scr = sorted(lst, reverse=True)
    mini = min(scr)
    maxi = max(scr)
    gap = 0
    for i in range(len(scr)-1):
        if gap < scr[i] - scr[i+1]:
            gap = scr[i]-scr[i+1]
    print(f'Class {z+1}')
    print(f'Max {maxi}, Min {mini}, Largest gap {gap}')