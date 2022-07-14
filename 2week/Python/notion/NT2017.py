# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지

A = input()
a = []
for i in range(len(A)):
    letter = ord(A[i])
    a.append(letter)

for i in range(len(A)):
    a[i] = chr(a[i]-32)
b = ''.join(a)
print(b)