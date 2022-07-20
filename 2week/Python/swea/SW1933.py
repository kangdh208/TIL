# 입력으로 1개의 정수 N 이 주어진다.

# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

n = int(input())
division = 1
lst = []
for i in range(1, n+1):
    if n % division == 0:
        lst.append(str(division))
        division += 1
    else:
        division += 1
print(' '.join(lst))