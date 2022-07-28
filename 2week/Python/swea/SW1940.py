# RC (Radio Control) 카의 이동거리를 계산하려고 한다.

# 입력으로 매 초마다 아래와 같은 command 가 정수로 주어진다.

# 0 : 현재 속도 유지.
# 1 : 가속
# 2 : 감속

# 위 command 중, 가속(1) 또는 감속(2) 의 경우 가속도의 값이 추가로 주어진다.

# 가속도의 단위는, m/s2 이며, 모두 양의 정수로 주어진다.

# 입력으로 주어진 N 개의 command 를 모두 수행했을 때, N 초 동안 이동한 거리를 계산하는 프로그램을 작성하라.

# RC 카의 초기 속도는 0 m/s 이다.

# 속도로 풀었을 때 > 음수인 경우 X
# T = int(input())
# result = []
# for z in range(T):
#     N = int(input())
#     distance = 0
#     velocity = 0
#     time = 0
#     for testcase in range(1, N+1):
#         change = list(map(int,input().split()))
#         if change[0] == 1:
#             velocity += change[1]
#             distance += velocity
#         elif change[0] == 2:
#             velocity -= change[1]
#             distance += velocity
#         else:
#             distance += velocity
#     result.append(distance)
# for i in range(T):
#     print(f'#{i+1} {result[i]}')

# 속력으로 풀었을 때 > 거리가 아닌 길이로
T = int(input())
result =[]
for i in range(T) :
    N = int(input())
    length = 0
    velocity = 0
    for i in range(N) :
        case = input().split()
        if case[0] == '0' :
            velocity = velocity
            length += velocity
        elif case[0] == '1' :
            velocity += int(case[1])
            length += velocity
        else :
            if int(case[1]) > velocity :
                velocity = 0
                length = length
            else :
                velocity -= int(case[1])
                length += velocity
    result.append(length)

for j in range(T):
    print(f"#{j+1} {result[j]}")