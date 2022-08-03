<h1> Algorithm 초급</h1>

<h2>
    스택(Stack)
</h2>


> 스택(Stack)은 쌓는다는 의미로써, 마치 접시를 쌓고 빼듯이 데이터를 한쪽에서만 넣고 빼는 자료구조
>
> 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 LIFO(Last-in First-out, 후입선출) 방식

<h3>
    스택 자료구조의 대표 동작
</h3>

- 스택에 새로운 데이터를 삽입하는 행위 ==> **push**
- 스택의 가장 마지막 데이터를 가져오는 행위 ==> **pop**
- 파이썬은 리스트(List)로 스택을 간편하게 사용할 수 있음
  - push ==> append
  - pop ==> pop

<h4>
    스택을 사용하는 순간
</h4>

1. 뒤집기, 되돌리기, 되돌아가기
   - 데이터를 뒤집어야 할 때
2. 마무리 되지 않은 일을 임시 저장

<h5>
    사용례
</h5>

- 괄호 매칭
  - 열렸는데 닫히지 않은 것들을 찾음

```python
map(int, input().split()) # 정상
map(int, input().split())) # 괄호가 잘못 들어갔다고 알림
```

- 함수 호출 (재귀 호출)

```python
print(sum(max(min(2, 5), 10), min(2, 5))) # 출력하려고 하니 함수가 끝나지 않음
>>> print(sum(max(2, 10), min(2, 5)))
>>> print(sum(10, min(2, 5)))
>>> print(sum(10, 2))
>>> 12
```

- 백트래킹
- 깊이 우선 탐색(DFS)

------

<h2>
    큐(Queue)
</h2>

> 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조
>
> 가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(First-in First-out, 선입선출) 방식

<h3>
    큐 자료구조의 대표 동작
</h3>

- 맨 뒤에 데이터를 삽입하는 행위 ==> enqueue
- 맨 앞 데이터를 가져오는 행위 ==> dequeue
- 파이썬은 리스트(List)로 큐를 간편하게 사용할 수 있음
  - enqueue ==> append
  - dequeue ==> pop(0)

<h3>
    큐의 단점 
</h3>

* 데이터를 뺄 때 큐 안에 있는 데이터가 많은 경우 비효율적이다
  - 맨 앞 데이터가 빠지면서, 리스트의 인덱스가 하나씩 당겨지기 때문
    - 큐보다는 덱을 활용하는 게 낫다

------

<h2>
    덱(Deque, Double-Ended)
</h2>

- 양 방향으로 삽입과 삭제가 자유로운 큐

  - 넣을 때 : 

- 삽입, 추출이 모두 큐보다 훨씬 빠름

- 파이썬은 `collections` 모듈에 `deque`라는 클래스로 이미 구현

  

```python
from collections import deque

d = deque()
print(type(d)) # <class 'collections.deque'>

# 스택이나 큐처럼 덱의 오른쪽에서 요소 삽입 : append
for i in range(10):
    d.append(i)
print(d) # deque([10,0,1,2,3,4,5,6,7,8,9])

# 덱의 왼쪽에서 요소 삽입 : appendleft
d.appendleft(10)
print(d) # deque([0,0,0,10,0,1,2,3,11,4,5,6,7,8,9])

# 덱의 중간에 요소 삽입 : insert
d.insert(5,11)
print(d) # deque([10,0,1,2,3,11,4,5,6,7,8,9])

# 덱의 왼/오른쪽에서 iterable한 객체를 통째로 append 하여 연장시키는 연산 : extendleft/extend
d.extend([0,0,0])
print(d) # deque([10,0,1,2,3,11,4,5,6,7,8,9,0,0,0])
d.extend([0,0,0])
print(d) # deque([0,0,0,10,0,1,2,3,11,4,5,6,7,8,9,0,0,0])

# 스택처럼 덱의 오른쪽에서 요소 삭제 : pop
for i in range(10):
    d.pop()
print(d) # deque([0,0,0,10,0,1,2,3])

# 큐처럼 덱의 왼쪽에서 요소 삭제 : popleft
for i in range(3):
    d.popleft()
print(d) # deque([10,0,1,2,3])

# 작업을 완료한 후에 일반적인 리스트처럼 이용 가능
print(list(d)) #[10,0,1,2,3]
```

***

<h2>
    힙 (Heap)
</h2>

> 우선순위 큐를 위하여 만들어진 자료구조

* 완전 이진 트리(Complete Binary Tree) 형태
  * 완전 이진 트리(Complete Binary Tree) 란 ?
    * 이진 트리에 노드를 삽입할 때 왼쪽부터 차례대로 삽입하는 트리

<h4>
    Heap VS Queue
</h4>

- 일반적인 큐(Queue)는 순서를 기준으로 가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(First-in First-out, 선입선출) 방식 >> 순서가 아닌 다른 기준일 경우는 힙(Heap)

* Heap 이 필요한 경우!!

  - 우선순위 큐(Priority Queue) 는 우선순위(중요도, 크기 등 순서 이외의 기준) 를 기준으로 가장 우선순위가 높은 데이터가 가장 먼저 나가는 방식

  - 순서가 아닌 우선순위를 기준으로 가져올 요소를 결정하는 큐
    - ex) 가중치가 있는 데이터, 작업 스케줄링, 네트워크

\----- 즉, 큐는 가장 오래된 데이터를 dequeue하지만 힙은 가장 작은 데이터를 heapq.heappop()

<h3>
    우선순위 큐(Priority Queue)를 구현하는 방법
</h3>

1. 배열(Array)
2. 연결 리스트(Linked List)
3. 힙(Heap)

\-------우선순위 큐 구현별 시간 복잡도

| 연산 종류                | Enqueue(추가) | Dequeue |
| ------------------------ | ------------- | ------- |
| 배열(Array)              | O(1)          | O(N)    |
| 정렬된 배열              | O(N)          | O(1)    |
| 연결 리스트(Linked List) | O(1)          | O(N)    |
| 정렬된 연결 리스트       | O(N)          | O(1)    |
| 힙(Heap)                 | O(logN)       | O(logN) |

<h3>
    힙(Heap)의 특징
</h3>

- 최대값 또는 최소값을 빠르게 찾아내도록 만들어진 데이터 구조
- 완전 이진 트리의 형태로 느슨한 정렬 상태를 지속적으로 유지
- 힙 트리에서는 중복 값을 허용

<h4>
    힙(Heap)을 사용하는 순간
</h4>

1. 데이터가 지속적으로 정렬되야 하는 경우
2. 데이터에 삽입/삭제가 빈번할 때

<h5>
    파이썬의 heapq 모듈
</h5>

- Minheap(최소 힙) 으로 구현되어 있음
  - 가장 작은 값이 먼저 옴
- 삽입, 삭제, 수정, 조회 와 같은 연산의 속도가 리스트보다 빠름
- 배열, 연결 리스트, 힙으로 구현 가능

<h3>
    Heap 구현 딕셔너리 메소드
</h3>

1. heapq.heapify()

```python
import heapq

numbers = [5, 3, 2, 4, 1] # 정렬되지 않은 데이터

heapq.heapify(numbers) # 원본을 바꾼다!!

print(numbers) # 1 3 2 4 5, 느슨한 정렬
```

2. heapq.heappop(heap)

```python
import heapq

numbers = [5, 3, 2, 4, 1] # 정렬되지 않은 데이터

heapq.heapify(numbers) # 원본을 바꾼다!!

heapq.heappop(numbers) # 맨 앞의 최소값만 빼면..

print(numbers) # 2 3 5 4!!! 최소값인 2가 앞으로!!!
```

3. heapq.heappush(heap, item)

```python
import heapq

numbers = [5, 3, 2, 4, 1] # 정렬되지 않은 데이터

heapq.heapify(numbers) # 원본을 바꾼다!!

heapq.heappop(numbers) # 맨 앞의 최소값만 빼면..

heapq.heappop(numbers)

heapq.heappush(numbers, 10) # 느슨하게 넣어주기

heapq.heappush(numbers, 0)

print(numbers) # 0 3 5 10 4
```

------

<h2>
    집합(셋,Set)
</h2>

> 셋(Set)은 수학에서의 '집합' 을 나타내는 데이터 구조

<h3>
	셋(set)의 연산
</h3>

1. .add()
2. .remove()
3. \+(합집합)
4. \- (차집합)
5. & (교집합)
6. ^ (대칭 차집합)

<h3>
    셋(Set) 을 사용
</h3>

1. 데이터의 중복이 없어야 할 때 (고유값들로 이루어진 데이터가 필요할 때)
2. 정수가 아닌 데이터의 삽입, 삭제, 탐색이 빈번히 필요할 때

셋(Set) 연산의 시간 복잡도

| 연산 종류   | 시간 복잡도 |
| ----------- | ----------- |
| 탐색        | O(1)        |
| 제거        | O(1)        |
| 합집합      | O(N)        |
| 교집합      | O(N)        |
| 차집합      | O(N)        |
| 대칭 차집합 | O(N)        |

