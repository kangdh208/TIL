# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.


def solution(my_str, n):
    answer = []
    if len(my_str) // n == 0:
        turn = len(my_str) // n - 1
    else:
        turn = len(my_str) // n
    for i in range(turn + 1):
        answer.append(my_str[n * i : n * (i + 1)])
    if answer[-1] == "":
        answer.pop()
    return answer
