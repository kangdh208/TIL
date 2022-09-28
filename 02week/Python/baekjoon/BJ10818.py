# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

n = int(input())
lst = map(int, input().split())
lst = list(lst)
a = max(lst)
b = min(lst)
print(b,a)