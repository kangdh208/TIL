# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

n0 = int(input())%42
n1 = int(input())%42
n2 = int(input())%42
n3 = int(input())%42
n4 = int(input())%42
n5 = int(input())%42
n6 = int(input())%42
n7 = int(input())%42
n8 = int(input())%42
n9 = int(input())%42
a = {n0, n1, n2, n3, n4, n5, n6, n7, n8, n9}
print(len(a))

number =[]
for i in range(10):
    n = int(input())%42
    number.append(n)
numbers = set(number)
print(len(numbers))
