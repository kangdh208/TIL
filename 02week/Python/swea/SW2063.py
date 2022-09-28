# 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.

# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.

# 런타임에러(답은맞는데)
N = int(input())
for i in range(N):
    lst = list(map(int, input().split()))
    j = int((len(lst)-1)/2)
    number = sorted(lst)
    print(number[j])

# 새풀이
n = int(input())
new = list(map(int, input().split()))
new.sort()
length = n // 2
print(new[length])