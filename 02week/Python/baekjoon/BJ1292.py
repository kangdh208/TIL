# 동호는 내년에 초등학교를 입학한다. 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.

# 이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.

# 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

# 시간초과
start, end = map(int,input().split())
num=1
while True:
    if num*(num-1)/2+1<start:
        num+=1
    else:
        break
num = num-1
mun=num
while True:
    if mun*(mun+1)/2<end:
        mun+=1
    else:
        break
mun = mun-1
middlesum = 0
u = num+1
while u!=mun+1:
    middlesum += u*u
    u+=1
frontsum = int(num*(num*(num+1)/2-start+1))
endsum = int((mun+1)*(end-mun*(mun+1)/2))
number = frontsum + middlesum+endsum
print(number)

#새풀이
s,e = map(int,input().split())
number = []
for i in range(46): # 범위가 1000
    for j in range(i):
        number.append(i)
print(number[s-1:e])
print(sum(number[s-1:e]))