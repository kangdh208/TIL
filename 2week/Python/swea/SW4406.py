# 불의의 교통사고를 당한 당신은 얼마 후 자신의 인식 속에서 모음이라는 것이 사라진 것을 알게 되었다.

# 알파벳 소문자 만으로 이루어진 단어를 당신은 어떤 식으로 보게 될까?

# 알파벳에서 모음은 ‘a’, ‘e’, ‘i’, ‘o’, ‘u’의 다섯가지로 예를 들어 “congratulation”이라는 단어를 당신이 보게 되면 “cngrtltn”으로 인식하게 될 것이다.

T = int(input())
for z in range(T):
    word = input()
    nwrd = ''
    for i in range(len(word)):
        if word[i] in 'aeiou':
            continue
        else:
            nwrd += word[i]
    print(f'#{z+1} {nwrd}')