# 카카오 코드 페스티벌에서 빠질 수 없는 것은 바로 상금이다. 2017년에 개최된 제1회 코드 페스티벌에서는, 본선 진출자 100명 중 21명에게 아래와 같은 기준으로 상금을 부여하였다.

# 순위	상금	인원
# 1등	500만원	1명
# 2등	300만원	2명
# 3등	200만원	3명
# 4등	50만원	4명
# 5등	30만원	5명
# 6등	10만원	6명
# 2018년에 개최될 제2회 코드 페스티벌에서는 상금의 규모가 확대되어, 본선 진출자 64명 중 31명에게 아래와 같은 기준으로 상금을 부여할 예정이다.

# 순위	상금	인원
# 1등	512만원	1명
# 2등	256만원	2명
# 3등	128만원	4명
# 4등	64만원	8명
# 5등	32만원	16명


# 제이지는 자신이 코드 페스티벌에 출전하여 받을 수 있을 상금이 얼마인지 궁금해졌다. 그는 자신이 두 번의 코드 페스티벌 본선 대회에서 얻을 수 있을 총 상금이 얼마인지 알아보기 위해, 상상력을 발휘하여 아래와 같은 가정을 하였다.

# 제1회 코드 페스티벌 본선에 진출하여 a등(1 ≤ a ≤ 100)등을 하였다. 단, 진출하지 못했다면 a = 0으로 둔다.

# 제2회 코드 페스티벌 본선에 진출하여 b등(1 ≤ b ≤ 64)등을 할 것이다. 단, 진출하지 못했다면 b = 0으로 둔다.

# 제이지는 이러한 가정에 따라, 자신이 받을 수 있는 총 상금이 얼마인지를 알고 싶어한다.

dic17 = {
    1 : 5000000,
    2 : 3000000,
    3 : 2000000,
    4 : 500000,
    5 : 300000,
    6 : 100000
}
dic18 = {
    1 : 5120000,
    2 : 2560000,
    3 : 1280000,
    4 : 640000,
    5 : 320000
}
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    prize = 0
    before = 0 #17 년도 누적합
    beforepeople = 1 # 17년도 등수
    while a > before:
        before += beforepeople
        beforepeople +=1
    # beforepeople -1 == 등수
    for k, v in dic17.items():
        if beforepeople-1 == k:
            prize += v
            # print(k, v , "+17")
    later = 0 # 18년도 누적합
    lateridx = 0 # 18년도 등수
    laterpeople = 1 #18년도 인원수
    while b > later:
        later += laterpeople
        lateridx +=1
        laterpeople = 2 ** lateridx
    for k, v in dic18.items():
        if lateridx == k:
            prize += v
            # print(k,v,'+18')
    print(prize)
# 새접근 >> 위에것 맞았으니 안할래(리스트로 푸는법)
ra17 = [1,3,6,10,15,21,100]
ra18 = [1,3,7,15,31,100]
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    for i in range(len(ra17)):
        if a<=ra17[i]+1:
            rank17 = i+1
    for k, v in dic17.items():
        if k == rank17:
            print(v)