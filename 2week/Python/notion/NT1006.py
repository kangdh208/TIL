# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류코드
# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)
# print(answer)
# 수정코드
N = 10
answer = [] # 튜플에서 리스트로
for number in range(N + 1):
    answer.append(number * 2)

print(answer)