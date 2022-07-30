# 학기가 끝나고, 학생들의 점수로 학점을 계산중이다.

# 학점은 상대평가로 주어지는데, 총 10개의 평점이 있다.
# A+ A0 A- B+ B0 B- C+ C0 C- D0

# 학점은 학생들이 응시한 중간/기말고사 점수 결과 및 과제 점수가 반영한다.

# 각각 아래 비율로 반영된다.

# 총점 = 중간고사(35%) + 기말고사(45%) + 과제(20%)

# 10 개의 평점을 총점이 높은 순서대로 부여하는데,

# 각각의 평점은 같은 비율로 부여할 수 있다.

# 예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.

# 입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고,

# 학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,

# K 번째 학생의 학점을 출력하는 프로그램을 작성하라.

T = int(input())
for z in range(T):
    N,K = map(int, input().split())
    scorelst = []
    for y in range(N):
        score = list(map(int, input().split()))
        personscore=score[0]*0.35+score[1]*0.45+score[2]*0.2
        scorelst.append(personscore)
    target = scorelst[K-1]
    scrlst = sorted(scorelst, reverse=True)
    for i in range(N):
        if target == scrlst[i]:
            rank = i
    hakjum = rank//(N//10)
    scrset = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    print(f'#{z+1} {scrset[hakjum]}')