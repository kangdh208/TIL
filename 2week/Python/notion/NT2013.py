# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
string = input()
reverse_string = string[::-1]
print(reverse_string)
# 같은 결과
a = input()
value = ''
for i in a:
    value = i + value
print(value)
# 같은 결과
b = input()
print(''.join(reversed(b)))
# 같은 결과
c = input()
for i in range(len(c)):
    print((c[len(c)-i-1]), end='')