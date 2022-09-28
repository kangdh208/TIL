# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 시간 초과
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ans = []
num = sorted(list(set(lst)))
for i in lst:
    ans.append(num.index(i))
print(*ans, sep=' ')

# 딕셔너리
N = int(input())
arr = list(map(int,input().split()))
array = list(sorted(set(arr)))
dic = {array[i]:i for i in range (len(array))}

for i in arr:
    print(dic[i],end=' ')