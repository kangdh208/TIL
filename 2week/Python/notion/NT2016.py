# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

A = input()
cnt = 0
a = []
for i in range(len(A)):
    letter = A[i]
    a.append(letter)
for i in range(len(A)):
    if a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u':
        cnt += 1
print(cnt)