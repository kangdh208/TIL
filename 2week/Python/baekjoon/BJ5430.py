# 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

# 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.

# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

# 뭐가틀렸지?
from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    if n == 0:
        a = input()
        lst = []
    else:
        lst = deque(map(int,(input().lstrip('[').rstrip(']')).split(',')))
    if lst:
        idx = 1
        for i in range(len(p)):
            if p[i] == 'R':
                idx *= -1
            if p[i] == 'D':
                if idx >0:
                    if lst:
                        lst.popleft()
                    else:
                        print('error')
                        break
                else:
                    if lst:
                        lst.pop()
                    else:
                        print('error')
                        break
        if lst:
            if idx > 0:
                lst = list(map(str,lst))
                print(f'[{",".join(lst)}]')
            else:
                lst = list(map(str,lst))
                lst = lst[::-1]
                print(f'[{",".join(lst)}]')
    else:
        print('error')
        break
    
# 긁풀
import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    if n == 0:
        arr = deque()

    flag = 0
    for j in p:
        if j == 'R':
            arr.reverse()
        elif j == 'D':
            if arr:
                arr.popleft()
            else:
                print("error")
                flag = 1
                break
    if flag == 0:
        print("["+",".join(arr)+"]")