# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

T= int(input())
result = []
for i in range(T):
    a,b = map(int, input().split(','))
    result.append(a+b)
for j in range(T):
    print(result[j])