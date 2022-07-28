# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.

# 이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.

# 다음과 같은 수 분포가 있으면,

# 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

# 최빈수는 8이 된다.

# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

# 런타임에러
N = int(input())
for z in range(1, 2*N+1):
    for k in range(N):
        testinput = int(input())
        scoreinput = list(input().split())
        cnt = {}
        for i in scoreinput:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
        maxkey = max(cnt, key = cnt.get)
        maxlst = [k for k, v in cnt.items() if max(cnt.values())==v]
for i in range(len(maxlst)):
    print(f'#{i+1} {maxlst[i]}')
# New Code
T = int(input())
for i in range(T):
    test_number = int(input())
    scores = list(map(int, input().split()))
    mode = 0  # 1

    # 2
    count_dic = {}
    for i in scores:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1
    # 3
    max_count = 0
    for key, value in count_dic.items():
        if max_count < value:  # 4
            max_count = value
            mode = key
        elif max_count == value:  # 5
            if mode < key:
                mode = key
    # 6
    print('#{} {}'.format(test_number, mode))
