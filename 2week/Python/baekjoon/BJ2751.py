# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
import sys
result =[]
for _ in range(int(sys.stdin.readline())):
    result.append(int(sys.stdin.readline()))
result.sort()
for i in range(len(result)):
    print(result[i])