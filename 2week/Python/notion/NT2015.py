# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

A = input()
cnt = -1
a = []
for i in range(len(A)):
    letter = A[i]
    a.append(letter)
for i in range(len(A)):
    if a[i] != 'a':
        cnt +=1
    elif a[i] == 'a':
        cnt +=1
        break
if cnt == len(A)-1:
    if a[cnt] =='a':
        cnt = len(A)-1
    else:
        cnt = -1
print(cnt)