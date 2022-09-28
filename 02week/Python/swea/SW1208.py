# 한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

# 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

# 평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.

# 평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.

# 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의한다.

for z in range(1,11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    for _ in range(dump+1):
        maxbox = max(boxes)
        minbox = min(boxes)
        boxes[boxes.index(maxbox)] -=1
        boxes[boxes.index(minbox)] +=1
    print(f'#{z} {maxbox - minbox}')