<h1> Python 초급</h1>

<h2>
    함수
</h2>

* 특정한 기능을 하는 코드의 조각(묶음)

* 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

* 기능

  * Decomposition(분해성) : 기능을 분해해서 재사용 가능

    ``` python
    # 코드로 작성할 경우
    numbers = [1, 10, 100]
    result = 0
    cnt = 0
      for number in numbers:
        result += number 
        cnt += 1
    print(result/cnt)
    
    # 함수사용할 경우
    print(sum(numbers)/len(numbers))
    ```

  * Abstraction(추상성) : 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음.(블랙박스) 재사용성, 가독성, 생산성

    ``` python
      print('happy!')
      # 함수 없이 구현하면 어셈블리어 기준 1500줄 이상
    ```

* 사용자 함수(Custom Function)

  * 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

    ``` python
    def add(a, b): # a, b를 더하는 함수를 선언
      return a+b
    
    add(5, 10) # 사용
    ```

* 기본 구조

  * 선언과 호출(define & call)

    * 선언은 def 키워드를 활용한다.

    * 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성

      • Docstring은 함수 body 앞에 선택적으로 작성 가능
      	• 작성시에는 반드시 첫 번째 문장에 문자열 ''' '''
  
    * 함수는 파라미터를 넘겨줄 수 있음
  
    * 함수는 동작 후에 return을 통해 결과값을 전달함
  
      ```python
      def foo(): # 함수의 선언
        return True
      foo() # 함수의 호출
      
      def add(x,y):
        return x + y
      add(2,3) # 5
      ```
  
      > 예시
  
      ```python
      num1 = 0
      num2 = 1
      
      def func1(a, b): # 3. 0 + 5 = 5
        return a + b
      
      def func2(a, b): # 4. 5 - 1 = 4
        return a - b
      
      def func3(a, b): # 2. 호출되는 함수 확인
        return func1(a, 5) + func2(5, b) # 5. 5 + 4 = 9
      
      result = func3(num1, num2) # 1. 호출
      print(result) # 6. 9
      ```
  
      
  
  * 입력(Input)
  
    * Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
  
    * Argument : 함수를 호출 할 때, 넣어주는 값

      * 필수 Argument : 반드시 전달되어야 하는 argument
      * 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달
  
      ```python
      def function(ham): # parameter : ham
        return ham
      
      function('spam') # argument : spam
      ```
  
      * positional arguments
  
        * 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨
      
          ```python
          def add(x, y):
            return x + y
          
          add(2, 3)# 2의 위치 x, 3의 위치 y
          ```
      
      * keyword arguments
      
        * 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
      
        * Keyword Argument 다음에 Positional Argument를 활용할 수 없음
      
          ``` python
          def add(x, y):
            return x + y
          
          add(x=2, y=5)
          add(2, y=5)
          ```
      
      
      * default arguments values
      
        * 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
      
        * 정의된 것 보다 더 적은 개수의 argument들로 호출될 수 있음
      
          ``` python
          def add(x, y=0):
            return x + y
          
          add(2)
          ```
      
      
      * 정해지지 않은 개수의 arguments
      
        * 여러개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
      
        * 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용
      
          ``` python
          def add(*args):
            for args in args:
              print(arg)
              
          add(2)
          add(2, 3, 4, 5) # 이 경우 타입이 tuple로 나옴
          ```
      
      
      * 정해지지 않은 개수의 keyword arguments
      
        * 함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정
      
        * Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현
      
          ``` python
          def family(**kwargs):
            for key, value in kwargs:
              print(key, ":", value)
              
          family(father='John', mother='Jane', me='Jone Jr.')
          ```


  * 범위(Scope)

    * 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

    * scope

      * global scope : 코드 어디에서든 참조할 수 있는 공간
      * local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능

    * 변수(variable)

      * global variable : global scope 내부에 정의된 변수

      * local variable : local scope 내부에 정의된 변수

        ```python
        def func(): 
          a = 20
          print('local', a)# local scope
          
        func() 
        print('global', a) # global scope
        # NameError : name 'a' is not defined // a가 정의되지 않은 오류 발생
        ```

  * 객체 수명주기

    * built-in scope `(print, sum, len..)`
      * 파이썬이 실행된 이후부터 영원히 유지됨
    * global scope `a=3`
      * 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    * local scope `def ___ a = 1..`
      * 함수가 호출될 때 생성되고, 함수가 종료될 때 까지 유지

  * 결과값(Output) : return

    * 함수는 반드시 값을 하나만 return
      * 명시적 return이 없는 경우에도 None을 반환
      
    * 함수는 return과 동시에 실행이 종료

      ```python
      def minus_and_product(x,y):
        return x - y
      	return x * y
      # x - y 만 실행이 되고 함수는 종료된다.
      
      def minus_and_product(x,y):
        return x - y, x * y
      
      minus_and_product(4, 5)
      # -> (-1, 20) 튜플 반환이 됨
      ```

* 이름 검색 규칙(Name Resolution)

  * 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음

  * 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름

    * Local scope : 함수
    * Enclosed scope : 특정 함수의 상위 함수
    * Global scope : 함수 밖의 변수, Import 모듈
    * Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성

  * 즉, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정 할 수 없음

    ```python
    print(sum)
    print(sum(range(2)))
    sum = 5
    print(sum)
    print(sum(range(2)))
    # TypeError TraceBack(most recent call last)
    # 3 sum = 5
    # 4 print(sum)---->
    # 5 print(sum(range(2)))
    # TypeError: 'int' object is not callable
    ```
<h2>
    Python 내장 함수
</h2>
<h3>
    map 함수(iterable;순회가능)
</h3>


> 순회 가능한 데이터구조(iterable)의 모든 요소에 함수 적용하고, 그 결과를 map object로 반환

```python
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(list(new_numbers))#[1, 2, 3]

n, m = map(int, input().split())
# int
# input() = 타입 : String(문자열)
# split() = 타입 : list(리스트)
# input().split = 타입 : list
# map = 어떤 함수를 반복가능한 것들의 요소에 모두 적용
# int 함수를 input().split() 리스트의 모든 요소에 적용한 결과 => map object n, m = [10, 20]

def plus10(n):
  return n + 10

numbers = [10, 20, 30]
new_numbers = list(map(plus10, numbers))
print(new_numbers)
#[20, 30, 40]
```

> 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때 사용

<h3>
    리스트 메서드
</h3>

* `input().split()`
  
  * input() 된 문자열을 공백 기준으로 분할
  * .split('-') 같은 형태로 변경가능
  
* `[리스트].append()`
  
  * 괄호 안의 내용을 리스트 후위에 추가
  
  * .extend(iterable) : 하나씩 하기 싫을 때
  
    * iterable에 무엇을 넣은가가 중요
  
  * 리스트에 iterable 추가함 
  
    ```python
    a = ['apple']
    a.extend('banana', 'mango')
    print(a)
    # typeerror : list.extend() takes
    
    # ('banana', 'mango') => (['banana', 'mango']) : 튜플이 아닌 리스트형태로 추가해야함
    # a.extend('banana') 문자열 하나씩 출력됨
    ```
    
    ```python
    a = [1, 2, 3]
    a = a.append(4)
    # 코드의 결과는 none
    # a.append(4) 의 return 값을 a에 저장한다. 
    # 리스트.append()의 메서드는 반환값이 none이다. 
    print(a)
    
    a = [1, 2, 3]
    a.append(4)
    print(a)
    
    a = [1, 2, 3]
    #sum 함수의 return 값을 변수 result에 할당 
    result = sum(a)
    ```
  
* `.insert(i, x)`
  
  * 정해진 위치에 i에 값을 추가함
* `.remove(x)`
  * 리스트에서 값이 x인 것 삭제
  * 리스트 가장 왼쪽에 있는 항목(첫번째) x를 제거
  * 항목이 존재하지 않을 경우 value error
* `.pop(i)`
  * 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환
  * i가 지정되지 않으면, 마지막 항목을 삭제하고 반환
* `.clear()`
  * 모든 항목을 삭제

<h3>
    문자열 메서드
</h3>

* 문자열 탐색 

  * `.find(x)` x의 첫 위치를 반환, 없으면, -1
  * `.index(x)` x의 첫번째 위치를 반환, 없으면, 오류발생

* 문자열 관련 검증 메소드 

  * `.isalpha()` : 알파벳인지 확인
  * `.isdigit()` : 숫자인지 확인
  * `.isupper()` : 대문자인지 확인
  * `.islower()` : 소문자인지 확인

* `.replace(old, new,[count])`   

  * `[,count]은 선택`
  * 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
  * count를 지정하면, 해당 개수만큼만 시행 

* `.strip([chars])`

  * 특정한 문자들을 지정하면, 양쪽을 제거(strip)하거나, 왼쪽을 제거(lstrip)하거나, 오른쪽을 제거(rstrip) 
  * 대부분 문자열을 지정하지 않으면 공백(space와 enter도 포함)을 제거할때 자주 사용

* `.split(sep=none, maxsplit=-1)`

  * 문자열을 특정한 단위로 나눠 리스트로 반환
  *  sep이 none이거나 지정되지 않으면 연속된 공백 문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음 
  * maxsplit이 -1인 경우에는 제한이 없음
* `'separator'.join([iterable])`

  * 반복가능한 컨테이너 요소들을 separator 로 합쳐 문자열 반환
  * iterable에 문자열이 아닌 값이 있으면  typeerror 발생

<h3>
    탐색 및 정렬
</h3>

* `.index(x)`


  * x값을 찾아 해당 index 값을 반환, 없는 경우 valueerror 발생

* `.count(x)`


  * 원하는 값의 개수를 반환 ; 리스트 순회

* `.sort()`


  * 리스트 항목 오름차순 배열

  * none반환

    ~~~python
    # 리스트_메서드 활용
    a = [10, 1, 100]
    # 정렬 (sort)
    new_a = a.sort() 
    print(a, new_a)
    # [10, 1, 100] none
    # 리스트 메서드에 활용하면, 그 메서드를 정렬된 상태로 변경(원본 변경)
    
    # 리스트에 sorted 함수를 활용
    b = [10, 1, 100]
    # 정렬(sorted)
    new_b = sorted(b) 
    print(b, new_b)
    # [10, 1, 100] [10, 1, 100]
    # sorted 함수를 활용하면, 원본을 변경하지 않음 
    # return되는 것은 정렬된 리스트
    ```
    ~~~

* `.reverse()`


  * 순서를 반대로 뒤집음, none반환
  * 정렬하는 것이 아님


> mutable(가변객체) 과 immutable(불변객체)
>
> ```python
> # 리스트는 mutable
> a = [1, 2, 3]
> a[0] = 100
> print(a)
> # [100, 2, 3] : 리스트는 가변
> 
> #문자열은 immutable
> a = 'hi'
> a[0] ='c'
> print(a)
> # 타입에러 : str object does not support item assignment : 문자열은 불변
> ```

<h3>
    딕셔너리 (키-값)
</h3>

* `.get(key[,default])`
  * key 를 통해 value 를 가져옴 
  * key error 가 발생하지 않으며 default 값을 설정 가능(none 기본)
* `.pop(key,[default])`

  * key가 딕셔너리에 있으면 제거하고 해당 값을 반환 
  * 그렇지 않으면 default 반환
  * default 값이 없으면 key error 발생 
* `.update([other])`

  * 값을 제공하는 key, value 로 덮어씀

```python
#기본순회
#키가 기준이고 직접 딕셔너리에 key로 접근하면 value를 얻을 수 있다. 
my_dict = {'apple': '사과', 'banana' : '바나나'}

for word in my_dict:
	print(word)

# apple
# banana


# value 접근
for word in my_dict:
	print(word, my_dict[word])
```

