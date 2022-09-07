# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

result =[]
for _ in range(int(input())):
    result.append(int(input()))
    result = sorted(result)
for i in range(len(result)):
    print(result[i])