# 문자열 word가 주어질 때, 해당 문자열에서 a 개수를 구하세요.
# count() 메서드 사용 금지
A = input()
cnt = 0
a = []
for i in range(len(A)):
    letter = A[i]
    a.append(letter)
for i in range(len(A)):
    if a[i] == 'a':
        cnt +=1
print(cnt)