# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

# 최댓값찾기
numbers =map(int, input().split())
number = list(numbers)
maxnum = number[0]
for i in range(1, len(number)):
    if maxnum <= number[i]:
        maxnum = number[i]

numlst = number
# 최댓값 리스트에서 제거한 새 리스트
for i in range(0, len(numlst)):
    if maxnum != numlst[i]:
        numlst[i] = number[i]
    else:
        numlst[i] = number[0]
print(numlst)
# 다음 최댓값찾기
second_maxnum = numlst[0]
for i in range(1, len(numlst)):
    if second_maxnum <= numlst[i]:
        second_maxnum = numlst[i]

print(second_maxnum)