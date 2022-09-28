# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

strin = input().upper()
strset = list(set(strin)) #중복 제거된 문자열
cntlst =[]
for i in strset:
    cnt = strin.count(i)
    cntlst.append(cnt) # 숫자 리스트에 추가

if cntlst.count(max(cntlst)) > 1 :  # 최대값 중복
    print('?')
else :
    max_location = cntlst.index(max(cntlst))  # 최대값 위치
    print(strset[max_location])