# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.


def solution(num, total):
    answer = []
    if num % 2 == 0:
        center = total // num
        left = num // 2 - 1
        right = num // 2
    elif num % 2 != 0:
        center = total // num
        left = num // 2
        right = num // 2
    for i in range(left):
        answer.append(center - left + i)
    answer.append(center)
    for i in range(1, right + 1):
        answer.append(center + i)
    return answer


print(solution(3, 12))
