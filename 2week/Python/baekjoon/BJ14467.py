# 닭이 길을 건너간 이유는 과학적으로 깊게 연구가 되어 있지만, 의외로 소가 길을 건너간 이유는 거의 연구된 적이 없다. 이 주제에 관심을 가지고 있었던 농부 존은 한 대학으로부터 소가 길을 건너는 이유에 대한 연구 제의를 받게 되었다.

# 존이 할 일은 소가 길을 건너는 것을 관찰하는 것이다. 존은 소의 위치를 N번 관찰하는데, 각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있다. 존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고, 소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.

# 이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자. 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.

# 뭐가틀린거지?
N = int(input())
road = {}
for _ in range(N):
    cow, crs = map(int, input().split())
    if cow in road:
        if road[cow] == crs:
            continue
        else:
            road[cow] += 1
    else:
        road[cow] = 1
cnt = 0
for k, v in road.items():
    back = int(v//2)
    cnt += back
print(cnt)

# 새풀이
n = int(input())
road = {}
cnt = 0
for i in range(n):
    cow,cross = map(int, input().split())
    if cow not in road:
        road[cow] = cross
    else:
        if road[cow] != cross:
            cnt +=1
            road[cow] = cross
print(cnt)