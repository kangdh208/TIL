# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# 오류코드
# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)
# 수정코드
word = "HappyHacking"

count = 0

for char in word:
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u": # 논리연산자 비교연산자 순서변경
        count += 1

print(count)