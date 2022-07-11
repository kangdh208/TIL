<h1> Python 기초</h1>

<h2>
    Computer Program?
</h2>

<h3>
    컴퓨터 프로그램의 특징
</h3>

> 컴퓨터 = 계산기 + 저장소

1) 우리는 일상생활에서 컴퓨터를 많이 사용한다.

2) 컴퓨터의 최대 장점: 반복적인 작업을 잘한다. 

3) 컴퓨터의 핵심: 범용성 
   * 예)스마트폰: 스마트폰에 앱(프로그램)을 설치하여 여러가지 작업 가능 

4) 컴퓨터에 일을 시키려면 인간이 컴퓨터에게 자세한 명령어(instruction)들을 주어야 한다.

5) 프로그램 (program) : 컴퓨터가 수행할 명령어를 적어 놓은 문서

6) 프로그램은 컴퓨터에만 설치되는 것이 아니다.

7) 임베디드 프로그램(embedded program): 전자기기에 내장되는 프로그램

8) 컴퓨터는 사람의 언어를 이해할 수 없다!

9) 기계어 (machine language) : 컴퓨터가 알아듣는 유일한 언어

10) 기계어는 0과 1로 구성된다. 

11) 초기의 컴퓨터에서는 기계어를 사용하여 프로그램을 했었다

<h2>
    Python?
</h2>

1) 1991년에 귀도 반 로섬(Guido van Rossum)이 개발한 대화형 프로그래밍 언어

2) 생산성이 뛰어남 

3) 초보자한테 좋은 언어, 같은 작업에 대해서도 `C`나 `Java`보다 간결하게 작성 가능

   ```java
   // Java로 작성시
   public class HelloPython {
       public static void main(String[] args){
           system.out.println("Hello Python!");
       }
   }
   ```

   ```python
   # Python으로 작성시
   print('Hello Python!')
   ```

4) 인터프리터 언어(해석기) : 파이썬은 실행 전에 컴파일 할 필요가 없음(타 언어들은 실행 전 컴퓨터가 이해할 수 있는 기계어로 컴파일 하는 과정이 필요

5) 파이썬은 문법이 쉬워서 코드를 보면 직관적으로 알 수 있는 부분이 많음

   ```python
   if "사과" in ["딸기", "바나나", "포도", "사과"]:    
   	print("사과가 있습니다")
   ```

6) 파이썬은 다양한 플랫폼에서 사용

7) 라이브러리가 풍부함

8) 애니메이션이나 그래픽을 쉽게 사용할 수 있음
9) 객체지향프로그래밍(OOP, Object Oriented Programming)
   * 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음
     * 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것 

<h4>
    주요 용어
</h4>

**스크립트 모드**

* 텍스트 에디터를 이용하여 명령어들을 파일에 저장한 후, 파일을 읽어 명령어들을 하나씩 실행할 수 있는 모드

* 코드가 복잡해지면 인터프리트 모드는 번거로우므로 스크립트 모드 사용

  ```html
  이렇게 한 줄씩 입력하다간 손가락이 남아나질 않겠네!!
  ```

**인터프리트 모드**

* 명령어를 한 줄씩 입력하여 실행하는 것은 초보 프로그래머한테 아주 편리한 기능
* 한 줄의 명령어를 입력하여 실행하고 결과를 즉시 알 수 있으며 현재 상태를 언제든 파악 가능
* 하지만 코드가 복잡해지면 인터프리트 모드는 아주 번거롭다.

**소스파일(Source File)**

* 텍스트 에디터를 이용하여 명령어들을 파일에 저장한 후에 파일을 읽어서 명령어들을 하나씩 실행하는 방법이 있으며 이 때 명령어들이 저장된 파일을 소스파일 이라함 

**변수(Variable)**

* 컴퓨터의 메모리 안에 만들어지는 공간

* 숫자나 문자를 저장할 수 있음 >>자료형

* 저장하는 표현은 아래와 같이 왼쪽(변수명) = 오른쪽(변수값-숫자/문자)

  ```python
  var = 11.0
  ```

**식별자(Identifier)**

* 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름

* 규칙

  * 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성

  * 첫 글자에 숫자가 올 수 없음

  * 길이제한이 없고, 대소문자를 구별

  * 다음의 키워드(keywords)는 예약어(reserved words)로 사용할 수 없음

    * ```python
      ['False', 'None', 'True', 'and', 'as', 'assert', 
      'async', 'await', 'break', 'class', 'continue', 
      'def', 'del', 'elif', 'else', 'except', 
      'finally', 'for', 'from', 'global', 'if', 
      'import', 'in', 'is', 'lambda', 'nonlocal', 
      'not', 'or', 'pass', 'raise', 'return', 'try', 
      'while', 'with', 'yield']
      ```

  * 키워드 / 예약어

    * ```python
      import keyword
      print(keyword.kwlist)
      ```
  
  * 내장함수나 모듈 등의 이름으로도 만들면 안됨
  
    * 기존의 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않음
  

<h2>
    자료형 : Type
</h2>
<h4>
    None
</h4>

* 파이썬 자료형 중 하나

* 파이썬에서는 값이 없음을 표현하기 위해 None 타입이 존재함.

* 일반적으로 반환 값이 없는 함수에서 사용하기도 함

  ```python
  print(type(None))
  #<class 'NoneType'>
  a = None
  print(a)
  #None
  ```

<h3>
    숫자형 자료형(Numeric Type)
</h3>

> **산술연산자** *(Arithmetic Operator)* :  기본적인 사칙연산 및 수식 계산

| 연산자 |   내용   |
| :----: | :------: |
|   +    |   덧셈   |
|   -    |   뺄셈   |
|   *    |   곱셈   |
|   /    |  나눗셈  |
|   //   |    몫    |
|   %    |  나머지  |
|   **   | 거듭제곱 |

> **복합연산자** *(In-place Operator) : 연산과 할당이 이루어짐



<h4>
    정수형(Numeric ; integer) : int
</h4>

* 모든 정수의 타입은 int
* Python 3부터는 long 타입은 없고, 모두 int로 표기 됨
* 여타 프로그래밍 언어, Python 2에서는 OS기준 32/64비트
* 매우 큰 수를 나타낼 때 오버플로우가 발생하지 않음
* 오버플로우(overflow) : 데이터 타입별로 사용할 수 있는 메모리의 크기를 넘어서는 상황
* Arbitrary Precision Arithmetic(임의 정밀도 산술)을 통해 고정된 형태의 메모리가 아닌 가용 메모리들을 활용하여 모든 수 표현에 활용

<h4>
    실수형(Numeric ; Floating Point Number) : float
</h4>

* 정수가 아닌 모든 실수는 float 타입

* 부동소수점

  * 실수를 컴퓨터가 표현하는 방법 - 2진수(비트)로 숫자를 표현
  * 이 과정에서 floating point rounding error가 발생하여, 예상치 못한 결과가 발생

  ```python
  11/2 #5.5
  type(10/3) #<class 'float'>
  
  10**100/3  #3.333333333333333e+99
  1/-10**100 #-1e-100
  1e-1        
  ```

  

* 부동소수점에서 실수 연산 과정에서 발생 가능

  * 값 비교하는 과정에서 정수가 아닌 실수인 경우 주의할 것

    ```python
    3.14 - 3.02 == 0.12
    #False
    #0.120000000000001 != 0.12
    ```

  * 매우 작은 수보다 작은지를 확인하거나 math 모듈 활용
  
    ```python
    # 1. 임의의 작은 수
    abs(a - b) <= 1e-10
    # 2. math 모듈 활용
    import math
    math.isclose(a, b)
    ```

<h4>
    복소수형(Numeric ; Complex Number) : complex
</h4>
* 실수부와 허수부로 구성된 복소수는 모두 complex 타입

  * 허수부를 j로 표현

    ```python
    a = 3+4j
    type(a)
    # <class 'complex'>
    a.real
    # 3.0
    a.imag
    # 4.0
    ```


<h4>
    불린형(Boolean) : Boolean
</h4>

* True / False 값을 가진 타입은 bool 

* 비교/논리 연산을 수행함에 있어서 활용됨

* 다음은 모두 False로 변환

  * 0, 0.0, (), [], {}, '', None

* **bool()함수**

  * 특정 데이터가 `True` 인지 `False`인지 반환

    ```python
    bool(0) #False
    bool(1) #True
    bool(-1) #True
    bool('') #False
    bool([]) #False
    bool([1,2,3]) #True
    ```

* 논리 연산자 (Logical Operator)

  * 논리식을 판단하여  `True` 인지 `False`인지 반환

  * | 연산자  |              내용              |
    | :-----: | :----------------------------: |
    | A and B |     A와 B모두 True시, True     |
    | A or B  |    A와 B모두 False시, False    |
    |   Not   | True를 False로, False를 True로 |

    * and : 모두 참인 경우 참, 그렇지 않으면 거짓

      | 논리연산자 and  | 내용  |
      | :-------------: | ----- |
      |  True and True  | True  |
      | True and False  | False |
      | False and True  | False |
      | False and False | False |

    * or : 둘 중 하나만 참이라도 참, 그렇지 않으면 거짓

      | 논리연산자 or  | 내용  |
      | :------------: | :---: |
      |  True or True  | True  |
      | True or False  | True  |
      | False or True  | True  |
      | False or False | False |

    * not : 참 거짓의 반대의 결과

      | 논리연산자 not | 내용  |
      | :------------: | :---: |
      |    not True    | False |
      |   not False    | True  |

      


<h4>
    문자형(String) : str
</h4>

* 큰따옴표(" ")나 작은따옴표('') 안에 들어있는 텍스트 데이터
* *반드시* 따옴표가 필요

<h4

<h4>
    리스트(list) : lst
</h4>



<h4>
    딕셔너리 : dic
</h4>



<h4>
    튜플 : tuple
</h4>



<h4>
    세트 : set
</h4>

> *비시퀀스형 컨테이너*

* 유일한 값들의 모임(Collection)
* 순서가 없고 중복된 값이 없음
  * 수학에서의 집합과 동일한 구조
* 변경 가능(mutable), 반복가능(iterable)
  * 단, 셋은 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음
* `중괄호{}` 혹은 `set()`을 통해 생성
* 순서가 없어 별도의 값에 접근 불가



<h3>
    함수
</h3>



<h5>print</h5>



<h5>
    range
</h5>



<h4>
    조건문
</h4>

```python
#예제
temp = 10
if temp > 20 :
	print("얇은 옷을 입으세요!") 
else:
	print("두꺼운 옷을 입으세요!") 
```



<h4>
    반복문
</h4>

> 입력문

```python
sign = "stop"

while sign == "stop":
	sign = input("현재 신호를 입력하시오: ")	
print("OK! 진행합니다.")
```

> 출력결과

```bash
현재 신호를 입력하시오: stop
현재 신호를 입력하시오: stop
현재 신호를 입력하시오: stop
현재 신호를 입력하시오: stop
현재 신호를 입력하시오: stop
현재 신호를 입력하시오: go
OK! 진행합니다.
```

