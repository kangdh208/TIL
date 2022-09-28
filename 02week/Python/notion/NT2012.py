# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오

a = input()
adel = a.replace('a', '')
print(adel)

#같은 결과
b = input()
char =''
for i in b:
    if i != 'a':
        char = char+ i

print(char)