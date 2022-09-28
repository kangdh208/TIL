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

# 리스트가 필요할까
b = input()
cnt1 = 0
for i in b:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        cnt1 += 1
print(cnt1)

#수업추가풀이
c = input()
cnt2 = 0
for i in c:
    if i in 'aeiou':
        cnt2 += 1
print(cnt2)

#한줄샷
d = input()
print(''in d)