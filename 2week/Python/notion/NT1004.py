# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류코드
# words = list(map(int, input().split()))
# print(words)
# 수정코드
words = list(input().split()) #숫자형에서 문자형으로
print(words) 