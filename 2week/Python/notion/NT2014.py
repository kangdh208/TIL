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

# 리스트는 필요 없음 사실 내 몸냥이주뭐
b = input()
cnt2 = 0
for i in b:
    if i == 'a':
        cnt2 +=1
print(cnt)