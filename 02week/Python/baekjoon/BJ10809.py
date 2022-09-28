# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
def alpha(a):
    lst = []
    for i in alphabet: #있니?
        n1 = str(a.find(i)) #있으면 어디니?
        lst.append(n1) #있으면 그자리에 추가해 없으면 -1
    result = " ".join(lst) #띄어쓰기 넣자
    return result

alphalst = [] #알파벳 리스트
for i in range(97, 123):
    alphalst.append(chr(i))
    alphabet = "".join(alphalst)

strinput = input()
print(alpha(strinput))

#같은결과

S = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    if i in S:
        print(S.index(i), end=" ")
    else:
        print(-1, end = ' ')