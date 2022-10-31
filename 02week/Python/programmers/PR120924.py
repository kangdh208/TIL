# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.


def solution(common):
    answer = common[-1]
    if common[1] - common[0] == common[2] - common[1]:
        answer += common[1] - common[0]
    elif common[1] / common[0] == common[2] / common[1] and common[1] / common[0] != 0:
        answer *= common[1] / common[0]

    return int(answer)


print(solution([0, 0, 0]))
