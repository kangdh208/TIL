# 1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

# 골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

def check(num):
    for i in range(2, int(num**0.5)+1):
        if num%i ==0:
            return False
    return True

T = int(input())

# 시간초과
# for z in range(T):
#     n = int(input())
#     result = []
#     for div in range(3, int(n/2)+1):
#         if check(div) == True and check(n-div) == True:
#             result.append(div)
#     keynum = max(result)
#     print(keynum, n-keynum)

# 새풀이
for z in range(T):
    n = int(input())
    n1 = n//2
    n2 = n//2
    while n1 > 0: #가운데서 출발하자
        if check(n1) and check(n2):
            print(n1, n2)
            break
        else:
            n1-=1
            n2+=1