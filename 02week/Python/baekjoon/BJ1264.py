# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

while True:
    inp = input()
    if inp != '#':
        cnt = 0
        for i in inp:
            if i in 'aeiouAEIOU':
                cnt +=1
        print(cnt)
    else:
        break