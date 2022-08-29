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

<h3>
    변수
</h3>

* 변수를 선언하는 규칙 세 가지
  * 이름은 의미있게 짓는다
  * 여러 단어를 연결한 변수 이름을 낙타 모양으로 만들어 준다
  * 변수 이름의 첫 글자는 반드시 문자나 밑줄(_), 달러 기호($)로 시작해야 한다.
* 변수 선언과 값/식 할당
  1. var 다음에 변수 이름을 적어서 변수를 선언하고,
  2. 변수 오른쪽에 = 기호를 붙이고 오른쪽에 저장할 값이나 식을 작성 (변수 선언과 값 할당을 동시에도 가능)

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
* 특징
  * 느슨한 자료형 체크(weak datatype check)
  * 자바스크립트는 미리 변수의 자료형을 지정하지 않음 
  * 변수를 지정하고 원하는 값을 할당만 하면 됨
* 종류
  * 기본형
    * 숫자(number)     : 따옴표 없이 표기한 숫자
    * 문자열(string)     : 작은 따옴표(')나 큰 따옴포(")로 묶어 나타냄
    * 논리형(boolean) : 참(true)/거짓(false)란 두 값만 가지고 있는 유형
    * undefined           : 변수를 선언하고 값을 저장하지 않는 등의 자료형을 지정하지 않았을 때. 
    * null                       : 값이 유효하지 않을 때
  * 복합형
    * 배열(array)           : 하나의 변수에 여러 값을 저장하는 유형
    * 객체(object)          : 함수의 속성이 함께 포함된 유형

**숫자형**  

* 정수 
  * 소수점 없는 숫자
  * 표현 방법에 따라 10진수, 8진수, 16진수
* 실수
  * 소수점이 있는 숫자
  * 자바스크립트에서는 정밀한 실수 계산을 못 함

**문자형**

- 작은 따옴표(‘ ‘) 나 큰 따옴표(“ “)로 묶은 자료

- 숫자도 따옴표로 묶으면 문자형이 됨.

- 따옴표 안에 따옴표를 넣어야 할 경우 ‘ ＂ ＂ ‘, 또는 ＂ ‘ ‘＂ 처럼 사용 

**논리형**

- 참(True)과 거짓(False)이라는 값을 표현하는 자료형 

- 프로그램에서 조건을 확인할 때 많이 사용 

**undefined**

- 자료형이 정의되지 않았을 때의 상태 

- 변수가 undefined라는 것은 ＇처음부터 변수에 값이 할당되지 않았다＇는 의미

**null**

- ‘처음에 할당된 값이 더 이상 유효하지 않다’는 의미

**배열**

- 하나의 변수에 여러 값 저장 

- 배열의 인덱스(index)는 0부터 시작

* 배열에 있는 값을 가져오려면 배열 이름과 대괄호([ ]) 안에 인덱스 사용

**객체**

- 여러 자료를 중괄호({ })로 묶은 것

- 키(key)와 값(value)을 한 쌍으로 여러 자료 저장

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

* 여러 명령을 늘어 놓지 않고 소스를 간단하게 작성할 수 있음

* 소스의 양이 줄어 실행 속도가 빨라짐

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
