# 육각형으로 이루어진 벌집이 있다. 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

# 출력초과
N = int(input())
n = N-1 #숫자가 0부터시작된다하자 > 6의 배수로 끊김
distance = 1 # 0으로 부터 거리
shell = distance - 1 # 껍질수 0:0, 1~6:1, 7~18:2 > 계차수열
point = 1 # 각 껍질의 마지막 수
while n>point: # 껍질 마지막수가 n보다 커질때까지
    cnt = 1 + 6*shell #한 껍질의 개수
    point = point + 6*cnt #마지막수 찾기
    distance += 1 #거리도 증가
    shell +=1
    print(shell, cnt, distance, point)
print(distance)

# 새접근 : 굳이 껍질수 말고 구할 필요가 있는가
n = int(input())
shell = 1
cnt = 1
while n>shell:
    shell += 6*cnt
    cnt += 1
print(cnt)