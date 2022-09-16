<h1>
    JavaScript
</h1>


<h2>
    Web Programming
</h2>

* 웹프로그래밍
  * 프로그래밍 : 사람이 원하는대로 컴퓨터가 작동할 수 있도록 컴퓨터 언어로 명령어를 나열하는 행위
  * 웹 프로그래밍 : ‘웹 브라우저’와 관련된 프로그램을 작성하는 것
    * 백엔드 (back-end) 프로그래밍 : 서버에서 데이터 관리를 프로그래밍 
    * 프런트엔드(front-end) 프로그래밍 : 서버에서 받아온 정보를 웹 브라우저에 어떻게 표시할 것인지 프로그래밍

<h2>
    Java Script
</h2>

* 역할
  * 웹 사이트를 동적으로 만들 수 있음
  * 웹 브라우저에서 실행되는 프로그램 제작 가능
  * 서버를 구성하고 서버용 프로그램 제작 가능(EX) 서버 제작시 JS 프레임워크인 Node.js사용)

* 특징
  * 모든 웹 브라우저에서 작동
  * 풀스택 웹 개발 뿐 아니라 다양한 용도의 프로그램 제작 가능
  * 다양한 자바스크립트 공개 API를 사용 가능
  * 다양한 라이브러리와 프레임워크를 사용 가능

<h3>
    소스작성 및 실행
</h3>
**\<script> 태그 안에 자바스크립트 작성**

1. \<script> 태그는 HTML 문서 어디에든 사용 가능
2. \<script> 태그는 한 문서 안에서 여러 개를 사용해도 됨
3. \<script> 태그가 삽입된 위치에서 소스가 실행됨

**외부 스크립트 파일 연결하기**

```html
<script src=”저장경로"> </script>
```

<h3>
    입력과 출력
</h3>

**사용자 입력값 받기**

> ```javascript
> prompt();
> #사용자에게 값을 입력받을 때 가장 쉽게 사용할 수 있는 함수
> ex) prompt("이름을 입력하세요.:");
> ```

**알림 창으로 출력하기** 

> ```javascript
> alert();
> # 웹 브라우저 화면에서 간단한 알림 내용을 출력 
> ```

**웹 브라우저 화면에 출력하기** 

> ```javascript
> document.write();
> # 결과값을 웹 브라우저 화면에 출력 
> var name = prompt("이름: ");
> document.write(name + "님, 환영합니다!");
> ```

**콘솔에 출력하기** 

> ```javascript
> console.log();
> # 괄호 안의 내용을 콘솔 창에 출력 
> var name = prompt("이름 : ");
> console.log(name + "님, 환영합니다!");
> ```

**그 외 규칙**

* 대소문자를 구별하여 소스를 작성
* 읽기 쉽도록 들여쓰기
* 세미콜론으로 문장을 구분
* 소스에 메모하려면 주석을 사용 
* 식별자는 정해진 규칙을 지켜 작성
* 예약어는 식별자로 사용할 수 없음

[환영합니다 예제](./Example/welcome.html)

```javascript
<body>
    <h1>안녕하세요</h1>
	<script>
    	// prompt()는 사용자로부터 입력받을때 사용
    	var name = prompt("이름을 입력하세요");
		// document(객체)는 현재 문서를 의미하고, write()는 출력함수
		document.write("<b>" + name + "</b>님, 환영합니다.");
	</script>
	<b>null</b>
	"님, 환영합니다. "
</body>
```

<h3>
    변수와 식별자
</h3>
* 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함

* 변수를 선언하는 규칙 세 가지
  
  * 이름은 의미있게 짓는다
  * 여러 단어를 연결한 변수 이름을 낙타 모양으로 만들어 준다
  * 변수 이름의 첫 글자는 반드시 문자나 밑줄(_), 달러 기호($)로 시작
  * 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
  * 예약어(for, if, function 등) 사용 불가능
  
* 변수 선언과 값/식 할당
  1. var 다음에 변수 이름을 적어서 변수를 선언하고,
  2. 변수 오른쪽에 = 기호를 붙이고 오른쪽에 저장할 값이나 식을 작성 (변수 선언과 값 할당을 동시에도 가능)
  
* 선언/할당/초기화


  * 선언(Declation)


    * 변수를 생성하는 행위 또는 시점

      ```javascript
      let foo // 선언
      console.log(foo) //undefined
      ```


  * 할당(Assignment)

    * 선언된 변수에 값을 저장하는 행위 또는 시점

      ```javascript
      foo = 11 // 할당
      console.log(foo) // 11
      ```


  * 초기화(Initialization)

    * 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

      ```javascript
      let bar = 0 // 선언 + 할당
      console.log(bar) // 0
      ```



<h4>
	let vs const vs bar
</h4>

  * let >> 재선언 불가능

  * const >> 재선언 불가능

  * var >> 재선언/재할당 모두 가능


    * 호이스팅 되는 특성으로 인해 예기치 못한 문제 발생 가능


      * 호이스팅(hoisting) : 변수를 선언 이전에 참조할 수 있는 현상


        * 변수 선언 이전의 위치에서 접근시 `undefined` 반환

        * JavaScript는 모든 선언을 호이스팅

        * 즉, var,let,const 모두 호이스팅 발생하지만 var는 선언과 초기화가 동시에 발생하므로 일시적 사각지대 존재하지 않음

          ```javascript
          console.log(username); // undefined
          var username = 'ABC';
          
          console.log(email); // Uncaught ReferenceError
          let email = 'ABC@gmail.com';
          
          console.log(age); // Uncaught ReferenceError
          const age = 50;
          ```

      * ES6이후 var 대신 const/let 사용 권장

      * 블록 스코프(block scope)


        * if,for,함수 등의 중괄호 내부를 가리킴

        * 블록 스코프를 가지는 변수는 블로 바깥에서 접근 불가능

          ```javascript
          let x = 1
          if (x === 1) {
              let x = 2;
              console.log(x); // 2
          };
          console.log(x);     // 1
          ```

      * 함수 스코프(function scope)


        * 함수의 줄괄호 내부

        * 함수 스코프를 갖는 변수는 함수 바깥에서 접근 불가능

          ```javascript
          function foo() {
              var x = 5;
              console.log(x); // 5
          };
          
          console.log(x)
          // ReferenceError: x is not defined
          ```



> 예제 : 나이계산기

```javascript
<script>
    function calc( ) {
    	var currentYear = 2022;
    	var birthYear = prompt("태어난 연도를 입력하세요.", "YYYY"); //프롬프트 창에 생년 입력
    	var age;
    	age = currentYear - birthYear + 1;
    	document.querySelector("#result").innerHTML = "당신의 나이는" + age +"세입니다.";
	}
</script>
```

<h3>
    자료형
</h3>

* 자료형은 컴표터가 처리하는 자료의 형태

* JavaScript 의  모든 값은 특정한 데이터 타입을 가짐

* 특징
  * 느슨한 자료형 체크(weak datatype check)
  * 자바스크립트는 미리 변수의 자료형을 지정하지 않음 
  * 변수를 지정하고 원하는 값을 할당만 하면 됨
  
* 종류
  * 기본형,원시타입(Primitive type)
    
    > 객체가 아닌 기본타입 : 변수에 해당 타입의 값이 담기며 다른 변수에 복사할 때 실제 값이 복사됨
    
    * 숫자(number)     : 따옴표 없이 표기한 숫자
    * 문자열(string)     : 작은 따옴표(')나 큰 따옴포(")로 묶어 나타냄
    * 논리형(boolean) : 참(true)/거짓(false)란 두 값만 가지고 있는 유형
    * undefined           : 변수를 선언하고 값을 저장하지 않는 등의 자료형을 지정하지 않았을 때. 
    * null                       : 값이 유효하지 않을 때
    
  * 복합형,참조타입(Reference type)
    
    > 객체 타입의 자료형 : 변수에 해당 객체의 참조 값이 담기며 다른 변수에 복사할 때 참조 값이 복사됨
    
    * 배열(array)           : 하나의 변수에 여러 값을 저장하는 유형
    * 객체(object)          : 함수의 속성이 함께 포함된 유형

**숫자형**  

* 정수, 실수 구분없는 하나의 숫자 타입

* 부동소수점 형시을 따름

  ```javascript
  const a = 13         // 양의 정수
  const b = -5         // 음의 정수
  const c = 3.14       // 실수
  const d = 2.998e8    // 거듭제곱
  const e = Infinity   // 양의 무한대
  const f = -Infinity  // 음의 무한대
  const g = NaN        // 산술 연산 불가
  ```

* 정수 
  * 소수점 없는 숫자
  * 표현 방법에 따라 10진수, 8진수, 16진수
* 실수
  * 소수점이 있는 숫자
  * 자바스크립트에서는 정밀한 실수 계산을 못 함
* NaN(Not-A-Number)
  * 계산 불가능한 경우 반환되는 값


**문자형**

* 텍스트 데이터를 나타내는 타입

- 작은 따옴표(‘ ‘) 나 큰 따옴표(“ “)로 묶은 자료

- 숫자도 따옴표로 묶으면 문자형이 됨

- 16bit 유니코드 문자의 집합

- 따옴표 안에 따옴표를 넣어야 할 경우 ‘ ＂ ＂ ‘, 또는 ＂ ‘ ‘＂ 처럼 사용 

  ```javascript
  const firstName = 'Brandon';
  const lastName = 'Elch';
  const fullName = '${firstName} ${lastName}'
  ```

> 문자열 관련 메서드

* string.includes(value);
  * 문자열에 value가 존재하는지 판별 후 참/거짓 반환
* string.split(value);
  * value가 없을 경우, 기존 문자열을 배열에 담아 반환
  * value가 빈 문자열일 경우 각 문자로 나눈 배열을 반환
  * value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환
* string.replace(from, to)
  * 문자열에 from 값이 존재할 경우, 1개만 to 값으로 교체하여 반환
* string.replaceAll(from, to)
  * 문자열에 from 값이 존재할 경우, 모두 to 값으로 교체하여 반환
* string.trim()
  * 문자열 시작과 끝의 모든 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
* string.trimStart()
  * 문자열 시작의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
* string.trimEnd()
  * 문자열 끝의 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환

**논리형(Boolean)**

- 참(True)과 거짓(False)이라는 값을 표현하는 자료형 

- 프로그램에서 조건을 확인할 때 많이 사용 

**undefined**

- 자료형이 정의되지 않았을 때의 상태 

- 변수가 undefined라는 것은 ＇처음부터 변수에 값이 할당되지 않았다＇는 의미

**null**

- ‘처음에 할당된 값이 더 이상 유효하지 않다’는 의미

- 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

- cf) null 타입은 원시타입에 속함 vs typeof연산자(자료형 평가를 위한 연산자)는 객체 자료로 표현

  ```javascript
  let firstName = null;
  console.log(firstName); // null
  
  typeof null // object
  ```

**배열**

- 하나의 변수에 여러 값 저장 

- 배열의 인덱스(index)는 0부터 시작

* 배열에 있는 값을 가져오려면 배열 이름과 대괄호([ ]) 안에 인덱스 사용

> 배열 관련 메서드

* array.reverse()

  * 원본 배열의 요소들의 순서를 반대로 정렬

* array.push()

  * 배열의 가장 뒤에 요소 추가

* array.pop()

  * 배열의 마지막 요소 제거

* array.unshift()

  * 배열의 가장 앞에 요소 추가

* array.shift()

  * 배열의 첫번째 요소 제거

* array.includes(value)

  * 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

* array.indexOf(value)

  * 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환
  * 만약 해당 값이 없을 경우 -1 반환

* array.join([separator])

  * 배열의 모든 요소를 연결하여 반환
  * separator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용

* Spread Operator 사용해서 배열내부에서 배열 전개 가능

  ```javascript
  const array = [1, 2, 3];
  const newArray = [0, ...array, 4];
  console.log(newArray) // [0, 1, 2, 3, 4]
  ```

> 배열 관련 메서드 - 순회시 특정 로직을 수행하는 메서드 , 호출시 인자로 callback 함수 받음

* array.forEach(callback(element[, index[, array]]))

  * 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  * 콜백 함수는 3가지 매개변수로 구성

    * element: 배열의 요소
    * index: 배열 요소의 인덱스
    * array: 배열 자체

  * 반환 값(return)이 없는 메서드

    ```javascript
    array.forEach((element, index, array) => {
        //do sth
    })
    ```

    ```javascript
    const fruits = ['berry', 'melon', 'apple', 'mango']
    
    fruits.forEach((fruit, index)) => {
        console.log(fruit, index)
        // berry 0
        // melon 1
        // apple 2
        // mango 3
    }
    ```

* array.map(callback(element[, index[, array]]))

  * 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  * 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환

  * 기존 배열 전체를 다른 형태로 바꿀 때 유용

    ```javascript
    array.map((element, index, array) => {
        //do sth
    })
    ```

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    
    const doubleNums = numbers.map((num) => {
        return num * 2
    })
    
    console.log(doubleNums) //[2, 4, 6, 8, 10]
    ```

* array.filter(callback(element[, index[, array]]))

  * 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  * 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

  * 기존 배열의 요소들을 필터링할 때 유용

    ```javascript
    array.filter((element, index, array) =>{
        // do sth
    })
    ```

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    const oddNums = numbers.filter((num, index) => {
        return num % 2
    })
    console.log(oddNums) // 1, 3, 5
    ```

* array.reduce(callback(acc, element, [index[, array]])[, initialValue])

  * 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  * 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

  * reduce 메서드의 주요 매개변수

    *  acc
      * 이전 callback 함수의 반환 값이 누적되는 변수
    * initialValue(optional)
      * 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값

  * 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

    ```javascript
    array.reduce((acc, element, index, array) => {
        //do sth
    }, initialValue)
    ```

    ```javascript
    const numbers = [1, 2, 3]
    const result = numbers.reduce((acc, num) => {
        return acc + num
    }, 0)
    
    console.log(result) // 6
    ```

* array.find(callback(element[, index[, array]]))

  * 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  * 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환

  * 찾는 값이 배열에 없으면 undefined 반환

    ```javascript
    array.find((element, index, array) {
         // do sth
    })
    ```

    ``` javascript
    const avengers = [
        { name: 'Tony Stark', age: 45}
        { name: 'Steve Rogers', age: 32}
        { name: 'Thor', age: 40}
    ]
    const result = avengers.find((avenger) => {
        return avenger.name === 'Tony Stark'
    })
    console.log(result) // { name: "Tony Stark", age: 45 }
    ```

* array.some(callback(element[, index[, array]]))

  * 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환

  * 모든 요소가 통과하지 못하면 거짓 반환

  * 빈 배열은 항상 거짓 반환

    ```javascript
    array.some((element, index, array) => {
        // do sth
    })
    ```

    ```javascript
    const numbers = [1, 3, 5, 7, 9]
    
    const hasEvenNumber = numbers.some((num) => {
        return num % 2 === 0
    })
    console.log(hasEvenNumber) // false
    
    const hasOddNumber = numbers.some((num) => {
        return num % 2
    })
    console.log(hasOdddNumber) // true
    ```

* array.every(callback(element[, index[, array]]))

  * 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환

  * 하나의 요소라도 통과하지 못하면 거짓 반환

  * 빈 배열은 항상 참 반환

    ```javascript
    array.every((element, index, array) => {
        // do sth
    })
    ```

    ```javascript
    const numbers = [2, 4, 6, 8, 10]
    
    const isEveryNumberEven = numbers.every((num) => {
        return num % 2 === 0
    })
    console.log(isEveryNumberEven) // false
    
    const isEveryNumberOdd = numbers.every((num) => {
        return num % 2
    })
    console.log(isEveryNumberOdd) // false
    ```

**객체**

- 여러 자료를 중괄호({ })로 묶은 것

- 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현

- key는 문자열 타입만 가능

  - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현

- value는 모든 타입(함수포함) 가능

- 객체 요소 접근은 점 또는 대괄호로 가능

  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

    ```javascript
    const me = {
        name: 'jack',
        phoneNumber: '01012345678', 'samsung': {
        	buds: 'galaxy buds pro',
        	galaxy: 'galaxy S20'
    	}
    }
    
    console.log(me,name) // jack
    console.log(me,phoneNumber)
    console.log(me['samsung']) // {buds: 'galaxy buds pro', galaxy: 'galaxy S20'}
    console.log(me['samsung'].buds) // galaxy buds pro
    ```

- 메서드는 객체의 속성이 참조하는 함수

- 객체.메서드명() 으로 호출 가능

- 메서드 내부에서는 this 키워드가 객체를 의미함

  ```javascript
  const me = {
      firstName: 'John',
      lastName: 'Doe',
      getFullName: function () {
          return this.firstName + this.lastName
      }
  }
  ```

<h3>
    JSON(JavaScript Object Notation)
</h3>

* key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
* 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입
  * 따라서 JS의 객체로써 조작하기 위해서는 구문 분석(parsing)이 필수
* 자바스크립트에서는 JSON을 조작하기 위한 두 가지 내장 메서드를 제공
  * JSON.parse()
    * JSON => 자바스크립트 객체
  * JSON.stringify()
    * 자바스크립트 객체 => JSON

<h3>
    연산자
</h3>

* 할당 연산자(복합대입연산자)
  * 변수에 값을 할당하는 연산자
  * 사칙 연산자와 조합해서 사용할 수 있음

| 할당 연산자 응용 | 예     | 의미      |
| ---------------- | ------ | --------- |
| +=               | a += b | a = a + b |
| -=               | a -= b | a = a - b |
| *=               | a *= b | a = a * b |
| /=               | a /= b | a = a / b |
| %=               | a %= b | a = a % b |

* 연결 연산자

  * 문자열과 문자열을 + 기호를 사용해 연결

* 동등 비교 연산자(==)

  * 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  * 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
  * 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
  * 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음

* 일치 비교 연산자(===)

  * 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  * 엄격한 비교(두 비교 대상의 타입과 값 모두 같은지 비교)가 이뤄지며 암묵적 타입 변환이 발생하지 않음

* 논리 연산자

  * and/or/not

    * and >> &&
    * or    >> ||
    * not  >> !

  * 단축평가 지원

    > false && true => false
    >
    > true || false  => true

* 삼항 연산자(Ternary Operator)

  * 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자

  * 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용

  * 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능

    ```javascript
    console.log(true ? 1 : 2);  // 1
    console.log(false ? 1 : 2); // 2
    
    const result = Math.PI > 4 ? 'Yes' : 'No';
    console.log(result); // No
    ```

* 형변환
  * 숫자형과 문자형을 더하면 숫자를 문자열로 인식함 
  * 곱하기나 나누기, 나머지 연산에서는 문자형 자료를 모두 숫자로 자동 인식함 

> 예제 : 할인 가격 계산 프로그램

```javascript
<script>
	function showPrice( ) {
    	var originPrice = document.querySelector('#oPrice').value;
    	var rate = document.querySelector('#rate').value;
    	var savedPrice = originPrice * (rate/100);
    	var resultPrice = originPrice - savePrice;
    	document.querySelector('#showResult').innerHTML = '원가격 '+originPrice +'원, 할인율' + rate + '이며, 할인금액 ' + savedPrice + '원으로 최종가 '+ resultPrice + '입니다.'
	}    
</script>
```

[나이계산기 예제](./Example/age.html)

[문자로 숫자받고 형태변환 예제](./Example/inputNum.html)

[할인가격 예제](./Example/sale.html)

[사각형 넓이 예제](./Example/square.html)

[텍스트 색변환 예제](./Example/text-color.html)

[시간 반환기 예제](./Example/time.html)

<h3>
    조건문 if
</h3>
**if 문**

괄호 안의 조건이 true이면 { } 사이의 명령을 처리하고, false 이면 { } 안의 명령 무시

**if … else 문**

if( ) 문의 괄호 안의 조건이 true이면 if 다음에 있는 { }의 명령을 처리하고, 

false 이면 else 다음에 있는 { } 안의 명령 실행

**조건 연산자** 

조건이 하나이고 실행할 명령도 하나일 때 `(조건)? 명령1 : 명령2` -> 삼항 연산자라고도 부름\

```javascript
var score = 75;
(score >= 60)? alert("통과") : alert("실패");
// 60이상에서 통과 그외는 실패
// 75이므로 통과
```

> 예제 : 3의 배수 검사기

```javascript
<script>
	var userNumber = prompt("숫자를 입력하세요 : ");
	var displayArea = document.querySelector('#result');
	if(userNumber != null) {
        if (userNumber % 3 === 0){
        	displayArea.innerHTML = userNumber + "은 3의배수입니다.";
    }
	else {
        displayArea.innerHTML = userNumber + "은 3의배수가 아닙니다.";
    }
}
</script>
```

> 예제 : switch문으로 여러 조건 값 확인하기

```javascript
<script>
		var session = prompt("관심 세션을 선택해 주세요. 1-마케팅, 2-개발, 3-디자인", "1");
	switch(session) {
        case "1" : document.write("<p>마케팅 세션은 <strong>201</strong>호입니다.</p>");
            break;
        case "2" : document.write("<p>개발 세션은 <strong>202</strong>호입니다.</p>");;
            break;
        case "3" : document.write("<p>디자인 세션은 <strong>203</strong>호입니다.</p>");;
            break;
        default: alert("잘못 입력했습니다.");
    }
</script>
```

[조건문 예제1](./Example/if-1.html) [조건문 예제2](./Example/if-2.html) [조건문 예제3](./Example/if-3.html) [조건문 예제4](./Example/if-4.html) [조건문 예제5](./Example/if-5.html) [조건문 예제6](./Example/if-6.html) [switch문 예제](./Example/switch.html) 

<h3>
    반복문 for
</h3>

* 카운터 변수를 기준으로 명령을 여러 번 실행

  ```javascript
  for (initialization; condition; expression) {
      // do sth
  }
  // initialization : 최초 반복문 진입 시 1회만 실행되는 부분
  // condition      : 매 반복 시행 전 평가되는 부분
  // expression     : 매 반복 시행 이후 평가되는 부분
  ```

* 여러 명령을 늘어 놓지 않고 소스를 간단하게 작성할 수 있음

* 소스의 양이 줄어 실행 속도가 빨라짐

* for ... of

  
  * 반복 가능한 객체(Array, Map, Set, String 등)를 순회하며 값을 꺼낼때 사용
  
* for ... in


  * 주로 객체(Object)의 속성들을 순회할 때 사용
  * 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음

  ```javascript
  var sum = 0;
  sum += 1;
  sum += 2;
  sum += 3;
  sum += 4;
  sum += 5;
  document.write("1부터 5까지 더하면 "+ sum);
  ```

  for사용시 아래같이 압축됨

  ```javascript
  var sum = 0;
  for(var i = 1; i < 6; i++) {
      sum += i;
  }
  document.write("1부터 5까지 더하면 "+ sum);
  ```

  > 예제 : 구구단 프로그램

  ```javascript
  //1번 방법
  for(var i=2; i<=9; i++) {
      document.write("<div>");
      for(var j=1; j<=9; j++) {
          document.write(i + "X" + j "=" + i*j + "<br>");
      }
      document.write("</div>");
  }
  ```

[for문 예제1](./Example/for-1.html) [for문 예제2](./Example/for-2.html) [for문 예제3](./Example/for-3.html) [for문 예제4](./Example/for-4.html) [for문 예제5](./Example/for-5.html) [중첩 for문 예제](./Example/double-for-1.html) 

<h3>
    반복문 while, do while
</h3>

> 반복 횟수 기준이라면 for 문을 쓰고 특정 조건에 따라 반복한다면 while문이나 do while문 사용

* 형식

```javascript
//while문
var i = 0;
while(i<10) {
    document.write('반복 조건이 true이면 반복합니다. <br>');
    i += 1;
}
//do while문
var i = 0;
do {
    document.write('반복 조건이 true이면 반복하며 초기값에 관계없이 무조건 1회 시행합니다. <br>');
    i+=1;
}while (i< 10);
```

> 예제 : 팩토리얼 계산 프로그램

```javascript
var n = prompt("숫자를 입력하세요.");
var nFact = 1;
var i = 2;
while (i <= n) {
    nFact *= i;
    i++;
}
document.write(n + "! = " +nFact);
```

[while문 예제](./Example/while.html) [무한while문 예제](./Example/while-unlimited.html) [do while문 예제](./Example/do-while.html) [do while문 예제2](./Example/do-while-user.html)

<h4>
    반복 제어
</h4>

* **break문**
  * 반복문의 흐름에서 바로 빠져나올 때 사용
* **continue문**
  * 주어진 조건에 맞는 값을 만났을 때 실행하던 반복 문장을 건너뛰고 반복문의 맨 앞으로 되돌아 감

[continue문 예제](./Example/continue.html)

<h3>
    함수
</h3>

* 참조 타입 중 하나로써 function 타입에 속함
* JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분
  * 함수 선언식 (function declaration)
  * 함수 표현식 (function expression)
* JavaScript의 함수는 일급 객체(First-class citizen)에 해당
  * 일급 객체: 다음의 조건들을 만족하는 객체를 의미함
    * 변수에 할당 가능
    * 함수의 매개변수로 전달 가능
    * 함수의 반환 값으로 사용 가능

<h5>
    함수의 정의
</h5>

* 함수의 이름과 함께 정의

* 이름(name) , 매개변수(args) , 함수 body(중괄호 내부)

  ```javascript
  function name(args) {
      // do sth
  };
  // 예시
  function add(num1, num2) {
      return num1 + num2;
  };
  ```

<h5>
    함수 표현식
</h5>

* 함수를 표현식(어떤 하나의 값으로 결정되는 코드의단위)내에서 정의하는 방식

* 익명함수(이름의 없는 함수) 로 정의 가능 >> 함수 표현식에서만 가능

* 인자 작성시 '=' 문자 뒤 기본 인자 선언 가능

  ```javascript
  const greeting = function (name = 'Anonymous') {
      return `Hi ${name}`
  };
  
  greeting() // Hi Anonymous
  ```

* 매개변수와 인자의 개수 불일치 허용

  * 매개변수 < 인자

    ```javascript
    const noArgs = function () {
        return 0;
    };
    
    noArgs(1, 2, 3); // 0
    
    const twoArgs = function (arg1, arg2) {
        return[arg1, arg2];
    };
    
    twoArgs(1, 2, 3) // [1, 2]
    ```

  * 매개변수 > 인자

    ```javascript
    const threeArgs = function(arg1, arg2, arg3) {
        return [arg1, arg2, arg3];
    };
    
    threeArgs()      // [undefined, undefined, undefined]
    threeArgs(1)     // [1, undefined, undefined]
    threeArgs(1, 2)  // [1, 2, undefined]
    ```

<h5>
    Rest Parameter
</h5>

* rest parameter(…)를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음

  * 만약 rest parameter로 처리한 매개변수에 인자가 넘어오지 않을 경우에는, 빈 배열로 처리

    ```javascript
    const restOper = function (arg1, arg2, ...restArgs) {
        return [arg1, arg2, restArgs];
    };
    
    restArgs(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
    restArgs(1, 2)          // [1, 2, []]
    ```

<h5>
    Spread Operator
</h5>

* spread operator(…)를 사용하면 배열 인자를 전개하여 전달 가능

  ```javascript
  const spreadOpr = function (arg1, arg2, arg3) {
      return arg1 + arg2 + arg3;
  };
  
  const numbers = [1, 2, 3];
  spreadOpr(...numbers) //6
  ```

<h5>
    함수의 타입
</h5>

* 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

  ```javascript
  // 함수 표현식
  const add = function (args) {};
  
  // 함수 선언식
  function sub(args) {};
  
  console.log(typeof add); // function
  console.log(typeof sub); // function
  ```

  * 함수선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생

    * 함수 호출 이후에 선언해도 동작

      ```javascript
      add(2, 7) // 9
      
      fucntion add (num1, num2) {
          return num1 + num2
      }
      ```

  * 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생

    * 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

      ```javascript
      sub(7, 2) // Uncaught ReferenceError: Cannot access 'sub' before initialization
      
      const sub = function(num1, num2) {
          return num1 - num2
      }
      ```

