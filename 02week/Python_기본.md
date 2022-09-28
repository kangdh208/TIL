<h1> Python 기본</h1>

<h2>
    기본 문법
</h2>

<h4>
    주석(Comment)
</h4>

* 코드에 대한 설명

  * 중요한 점이나 다시 확인하여야 하는 부분을 표시
  * 컴퓨터는 주석을 인식하지 않음 사용자만을 위한 것

* 가장 중요한 습관

  * 개발자에게 주석을 작성하는 습관은 매우 중요

  * 쉬운 이해와 코드의 분석 및 수정이 용이

    ✓ 주석은 코드 실행에 영향을 미치지 않을 뿐만 아니라

    ✓ 프로그램의 속도를 느리게 하지 않으며, 용량을 늘리지 않음

* 한 줄 주석

  * 주석으로 처리될 내용 앞에 ‘#’ 을 입력

  * 한 줄을 온전히 사용할 수도 있고, 그 줄 코드 뒷부분에 작성 할 수 있음

    ```python
    # 주석(comment)입니다. 
    # print('hello')
    print('world’) # 주석
    ```

<h4>
    input([prompt]) : 사용자입력
</h4>

* 사용자로부터 값을 즉시 입력 받을 수 있는 내장함수

* 대괄호 부분에 문자열을 넣으면 입력 시, 해당 문자열을 출력할 수 있음

* 반환값은 항상 문자열의 형태로 반환

  ```python
  name = input('이름을 입력해주세요 : ')
  print(name)   # 이름을 입력해주세요 : 파이썬
  type(name)    # str
  ```

<h4>
    숫자함수
</h4>

|  함수   | 내용                      | 함수  | 내용                           |
| :-----: | ------------------------- | :---: | ------------------------------ |
|  abs()  | 절대값 계산               | max() | 매개변수 값들 중 최대값을 반환 |
| round() | 소수 첫째 자리에서 반올림 | min() | 매개변수 값들 중 최소값을 반환 |
| sqrt()  | 제곱근을 구함             |       |                                |

***

<h2>
    제어문(Control Statement)
</h2>

* 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행하며, 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복하는 제어가 필요함)하는 문장


<h4>
    조건문 if
</h4>

> 형식


```python
if < expression >;
    # Run this Code block    <- 참일때 실행
else:
    # Run this Code block    <- 거짓일때 실행(선택적, 직접조건X)
```

> 조건표현식 코드

```python
value = num if num >= 0 else -num # 절댓값코드(조건표현식코드)
# 같은코드(조건문코드)
value = num
if num>=0:
    value = num
else:
    value = -num
```

* 조건에 따라 결정을 내리는 문장
* if – else 문은 조건에 따라서 2개 중에서 하나를 선택해야 하는 경우에 사용되는 문장
  * if – else문은 주어진 조건식을 계산하여 조건식이 참(true)으로 계산되면 if 아래에 있는 문장을 실행하고 거짓이면 else 아래의 문장을 실행
  * 때에 따라 else문은 생략이 가능

* 복수조건문 if–else 문은 조건에 따라 여러개 중에서 하나를 선택해야 하는 경우에 사용되는 문장
  * if–else 문은 위에서부터 코드를 읽어가며 해당하는 조건의 문장을 실행
  * 때에 따라 else문은 생략이 가능하며 else문 사용시에 조건은 추가해서는 안됨
* 중첩조건문은 조건문내에 조건문이 중첩되어 있는 형태
  * if~else 구문 안에는 여러 개(무제한)의 if~else 구문이 포함될 수 있으며 들여쓰기로 중첩의 수준을 알 수 있음

<h4>
    반복문 while
</h4>
> 형식

```python
while <expression>:
    # Code block
```

> 예제

```python
# <실습문제>
# 1부터 사용자가 입력한 양의 정수까지 총합을 구하는 코드를 작성하시오

# <풀이 절차>
# 매 회 n 이 1씩 증가해야하고
# 매 회 result 에는 n을 더해야함
# 종료는 n = user_input 보다 커졌을 때
# (True일땐 작거나 같을 때)

n = 0                       # 처음 시작 값
result = 0                  # 0부터 더하기 위해서
user_input = int(input())   # user_input 값
while n <= user_input:
    result += n
    n += 1
print(result)
```

* 어떤 조건을 정해 놓고 반복을 하는 구조
* 반복을 결정하는 조건이 있고 조건이 참이면 반복을 하고 그렇치 않으면 반복 루프를 빠져나감
* while문의 옆에 반복의 조건을 기술하고, 조건이 만족되는 동안 블록 안의 문장이 반복 실행

<h4>
    반복문 for
</h4>
> 형식

```python
for <변수명> in <반복 가능한 아이(iterable)>:
    # Code block
```

> 예제

```python
# 사용자가 입력한 문자를 한 글자씩 세로로 출력
chars = input()
# hi 출력

for char in chars:
    print(char)
# h
# i 출력
```

* for문은 시퀀스(스트링, 튜플, 리스트 ..)를 포함한 순회가능한 객체(iterable)요소를 모두 순회함

* 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음

* range를 써서 index 기준으로 문자열 순회 가능

> enumerate 순회

> 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환[(index, value) 형태의 tuple로 구성된 열거 객체를 반환]
>
> 튜플을 활용 : 알고리즘 때 잘 안쓰고, range 위주로 많이 사용하게 됨
>
> 딕셔너리 순회 : 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

```python
grade = {'john': 80, 'eric': 90}
for name in grade:
    print(name)
    
# john
# eric      이와 같이 키만 출력됨

+++++++++++++++++++++++++++++++

# 위의 상황에서 값과 같이 출력하고 싶다면?

grade = {'john': 80, 'eric': 90}
for name in grade:
    print(name, grades[name])

# john 80
# eric 90    이와 같이 키-값이 같이 출력됨
```

**반복문 제어**

* break: 반복문을 종료

  * break 통해 중간에 종료되는 경우 else문은 실행되지 않음

  ```python
  # break문을 만나면 반복문은 종료됨
  
  # 상황1
    n = 0
    while True:
        if n == 3:
              break
        print(n)
        n += 1
  # 0
  # 1
  # 2
          
  # 상황2
    for i in range(10):
          if i > 1:
              print('0과 1만 필요해!')
              break
          print(i)
  # 0
  # 1
  # 0과 1만 필요해!
  ```

* continue: continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

  ```python
  # continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
  
  for i in range(6):
      if i % 2 == 0
          continue
      print(i)
  # 1
  # 3
  # 5
  ```

* for-else: 끝까지 반복문을 실행한 이후 else문 실행

  ```python
  #상황1
    for char in 'apple':
        if char == 'b':
            print('b!')
            break
    else:
        print('b가 없습니다.')
  # b가 없습니다.
      
  #상황2
    for char in 'banana'
        if char == 'b'
            print('b!')
            break
    else:
        print('b가 없습니다.')
  # b!
  ```

  
