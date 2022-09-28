# 은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

# N이 주어졌을 때, N보다 작거나 같은 금민수 중 가장 큰 것을 출력하는 프로그램을 작성하시오.

N = int(input())
for i in range(N):
    num = str(N-i)
    cnt = 0
    for j in range(len(num)):
        if num[j] == '4' or num[j] == '7':
            cnt +=1
    if cnt == len(num):
        print(int(num))
        break