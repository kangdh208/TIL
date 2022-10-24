# 꿍은 도비에게 영어단어들을 제시한 후 어떤 단어가 대소문자를 구분하지 않고 사전순으로 가장 앞서는지 맞추면 양말을 주어 자유를 얻게해준다고 하였다.

# 하지만 인성이 좋지 않은 꿍은 사실 그러고 싶지 않았기 때문에 대소문자를 마구 섞어가며 단어들을 제시했다. 예를 들어, apPle은 Bat보다 앞서지만 AnT보다는 뒤에 있는 단어다.

# 도비에게 희망은 여러분뿐이다! 여러분이 도비에게 자유를 선물해주도록 하자!

while True:
    N = int(input())
    if N == 0:
        break
    lst = []
    for _ in range(N):
        lst.append(input())
    lst.sort(key=str.upper)
    print(lst[0])
