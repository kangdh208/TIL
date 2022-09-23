# 다솜이는 기타를 많이 가지고 있다. 그리고 각각의 기타는 모두 다른 시리얼 번호를 가지고 있다. 다솜이는 기타를 빨리 찾아서 빨리 사람들에게 연주해주기 위해서 기타를 시리얼 번호 순서대로 정렬하고자 한다.

# 모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.

# 시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.

# A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
# 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
# 시리얼이 주어졌을 때, 정렬해서 출력하는 프로그램을 작성하시오.

N = int(input())
serial = []
for _ in range(N):
    serial.append(input())

for i in range(N-1):
    for j in range(i+1, N):
        if len(serial[i]) > len(serial[j]):
            serial[i], serial[j] = serial[j], serial[i]
        elif len(serial[i]) == len(serial[j]):
            asum = 0
            bsum = 0
            for a, b in zip(serial[i], serial[j]):
                if a.isdigit():
                    asum += int(a)
                if b.isdigit():
                    bsum += int(b)
            if asum>bsum:
                serial[i], serial[j] = serial[j], serial[i]
            elif asum == bsum:
                for a, b in zip(serial[i], serial[j]):
                    if a>b:
                        serial[i], serial[j] = serial[j], serial[i]
                        break
                    elif a<b:
                        break
for i in serial:
    print(i)