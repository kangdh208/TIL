# 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -2^62보다 크거나 같고, 2^62보다 작거나 같다.

# 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

# 시간초과
N = int(input())
number = {}
for z in range(N):
    num = int(input())
    if num in number:
        number[num]+=1
    else:
        number[num] = 1
many = []
lotsofnum = max(number.values())
for k, v in number.items():
    if v == lotsofnum:
        many.append(k)
many=sorted(many)
print(many[0])