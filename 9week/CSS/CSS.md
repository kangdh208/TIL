<h1>
    CSS
</h1>


<h2>
    Web Programming
</h2>

* 웹프로그래밍
  * 프로그래밍 : 사람이 원하는대로 컴퓨터가 작동할 수 있도록 컴퓨터 언어로 명령어를 나열하는 행위
  * 웹 프로그래밍 : ‘웹 브라우저’와 관련된 프로그램을 작성하는 것
    * 백엔드 (back-end) 프로그래밍 : 서버에서 데이터 관리를 프로그래밍 
    * 프론트엔드(front-end) 프로그래밍 : 서버에서 받아온 정보를 웹 브라우저에 어떻게 표시할 것인지 프로그래밍
* 크롬 개발자 도구

  * 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공

    * 주요 기능 

      * Elements – DOM 탐색 및 CSS 확인 및 변경 
      * Styles – 요소에 적용된 CSS 확인 
      * Computed – 스타일이 계산된 최종 결과 
      * Event Listeners – 해당 요소에 적용된 이벤트 (JS) 

    * Sources, Network, Performance, Application, Security, Audits 등


***

<h2>
    CSS
</h2>


> Cascading Style sheets
>
> HTML이나 XML로 작성된 문서의 표시 방법을 기술하기 위한 스타일 시트

```css
/*
선택자 {
    (스타일 속성): (스타일 값);
}
예시
*/
text-Atype {
    color: blue;
    font-size: 15px;
}
```

* CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
* 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
* 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  * 속성 (Property) : 어떤 스타일 기능을 변경할지 결정 
  * 값 (Value) : 어떻게 스타일 기능을 변경할지 결정

<h3>
    CSS 정의 방법
</h3>

1. 인라인(inline)

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
   	<meta charset="UTF-8">
   	<meta name="viewport" content="width=device-width, initial-scale=1.0">
   	<title>Document</title>
   </head>
   <body>
   	/* 이부분 */
       <h1 style="color: blue; font-size: 100px;">Hello</h1>
   </body>
   </html>
   ```

2. 내부참조(embedding) - `<style>`

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
   	<meta charset="UTF-8">
   	<meta name="viewport" content="width=device-width, initial-scale=1.0">
   	<title>Document</title>
   	/* 이부분 */
       <style>
   		h1 {
   			color: blue;
   			font-size: 100px;
   		}
   	</style>
       /* 이부분 */
   </head>
   <body>
   </body>
   </html>
   ```

3. 외부참조(link file) - 분리된 CSS파일

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
   	<meta charset="UTF-8">
   	<meta name="viewport" content="width=device-width, initial-scale=1.0">
   	<title>Document</title>
   	<link rel='sytlesheet' href="mystle.css"> 
       /* 이부분을 적용 */
   </head>
   <body>
       <h1>
           이부분에 적용
       </h1>
   </body>
   </html>
   ```

<h3>
    기초 선택자
</h3>

* 요소 선택자
  * HTML 태그를 직접 선택
* 클래스(class) 선택자
  * 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택
* 아이디(id) 선택자 
  * \#문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  * 일반적으로 하나의 문서에 1번만 사용
  * 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장

<h3>
    속성 
</h3>

<h4>
    박스 모델
</h4>

* width, height : 요소의 가로/세로 너비

  - 기본값: auto / 브라우저가 너비를 계산

  - 단위: px, em, vw 등

* `<span></span>`

  - 인라인 요소

  - 기본값
    - 가로, 세로: 요소 내용에 맞게 자동으로 축소

  - 어차피 인라인 요소라 명시적으로 width, height를 설정해도 반영되지 않는다.

* `<div></div>`

  - 블럭 요소

  - 기본값

    - 가로: 부모 요소의 크기만큼 자동으로 늘어남 = 최대한 확대
    - 세로: 요소 내용에 맞게 자동으로 축소 = 최대한 축소

    ```html
    <!-- html -->
    <div class="parent">
      <div class="child"></div>
    </div>
    /* css */
    .parent {
      width: 100px;
      height: 50px;
      background-color: royalblue;
    }
    .child {
      /* width 기본값: 부모 요소의 가로 너비만큼 */
      height: 25px;
      background-color: orange;
    }
    ```

* max-width, max-height : 요소의 가로, 세로 너비의 상한

  - 기본값: none / 너비 제한 없음

    ```html
    /* css */
    .parent {
      width: 100px;
      height: 50px;
      background-color: royalblue;
    }
    .child {
      max-width: 50px;
      height: 25px;
      background-color: orange;
    }
    ```

* min-width, min-height : 요소의 가로, 세로 너비의 하한

  - 기본값: 0 / 너비 제한 없음. 요소의 크기는 0 이상의 수.

    ```css
    /* css */
    .parent {
      width: 100px;
      height: 50px;
      background-color: royalblue;
    }
    .child {
      min-width: 125px;
      height: 25px;
      background-color: orange;
    }
    ```

<h4>
    CSS 단위
</h4>

- px 픽셀

- % 상대적 백분율 - 기준이 필요

- 뷰포트 너비의 백분율

  - 1 vw: 뷰포트 가로 너비의 1%
  - 1 vh: 뷰포트 세로 너비의 1%*

- 글꼴 크기가 기준인 단위

  - rem 루트(

    ```
    <html></html>
    ```

    ) 요소의 글꼴 크기

    - 1 rem: 루트 요소의 글꼴 크기의 1배
    - html 요소의 기본 글꼴 크기는 16px
    - 1rem = 16px

  - em 요소의 글꼴 크기

    - font-size를 별도로 설정하지 않으면 상속에 의해 1 em = 16px
    - **요소에 설정된 font-size에 따라 1em의 크기가 달라지므로 주의**

    ```html
    <!-- html -->
    <div class="parent">
      <div class="child_em"></div>
      <div class="child_rem"></div>
    </div>
    /* css */
    .parent {
      width: 160px;
      height: 50px;
      background-color: royalblue;
      font-size: 8px;
    }
    .child_em {
      width: 10em;  /* 상속에 의한 글꼴 크기 8px * 10 = 80px */
      height: 50%;  /* 부모 요소 세로 너비의 50% */
      background-color: orange;
    }
    .child_rem {
      width: 10rem;  /* 루트 요소 글꼴 크기 16px * 10 = 160px */
      height: 50%;
      background-color: red;
    }
    ```

* 단축 속성

  >  넘겨주는 값의 갯수에 따라 여러 속성에 값을 부여할 수 있는 속성

<h4>
    margin: 외부 여백
</h4>

> 요소의 외부 여백을 지정하는 단축 속성

* 속성값

  - 기본값: 0 / 외부 여백 없음. 음수 사용 가능.

  - auto: 가로 너비가 명시된 블록 요소를 좌우 가운데 정렬시킴. (브라우저가 자동으로 계산)

  - 음수값

    ```html
    <!-- html -->
    <div class="container">
      <div class="item_0"></div>
      <div class="item_1"></div>
    </div>
    /* css */
    .container .item_0 {
      width: 100px;
      height: 100px;
      background-color: orange;
      border: 4px solid red;
      margin: 20px;
    }
    .container .item_1 {
      width: 100px;
      height: 100px;
      background-color: orange;
      border: 4px solid red;
      margin-left: 20px;
      margin-top: -50px;  /* 음수값 margin */
    }
    ```

* margin이 음수인 요소는 요소 경계를 넘어 밀려 들어가게됨

* 단축 속성 - 넘겨주는 값의 수에 따라 상하좌우 따로 margin 설정이 가능

  - 값 1개 ➡ 상하좌우 margin 설정
    ex) margin: 5px; ➡ 상하좌우 모두 5px

  - 값 2개 ➡ 상하 / 좌우 margin 설정
    ex) margin: 5px 10px; ➡ 상하 5px / 좌우 10px

  - 값 3개 ➡ 상 / 중(좌우) / 하 margin 설정
    ex) margin: 5px 10px 15px; ➡ 상 5px / 좌우 10px / 하 15px

  - 값 4개 ➡ 시계방향순으로(상 / 우 / 하 / 좌) margin 설정
    ex) maring: 5px 10px 15px 20px; ➡ 상, 우, 하, 좌 순으로

* 개별 속성
  - margin-top, margin-bottom, margin-left, margin-right

<h4>
    padding: 내부 여백
</h4>

> 요소의 내부 여백

* 속성값

  - 기본값: 0 / 내부 여백 없음

  - % 단위일 경우: 부모 요소의 가로 너비에 대한 비율

  - 요소 내부에 여백이 생기므로 요소 크기가 커진다.

* 단축 속성 / 개별 속성: margin과 동일

  ```html
  <!-- html -->
  <div class="container">
    <div class="item"></div>
    <div class="item"></div>
  </div>
  .container .item {
    width: 50px;
    height: 50px;
    background-color: royalblue;
    border: 5px solid orange;
  }
  .container .item:first-child {
    padding: 20px;
  }
  ```

<h4>
    border: 테두리
</h4>

> 요소의 테두리 선을 지정하는 단축 속성
> padding과 마찬가지로 크기가 커진다.

* 개별 속성

  - border-width: 선 두께 / 기본값 medium
    - 단축 속성: margin, padding과 동일
      - 키워드: medium, thin, thick - 모호한 값으로 사용 지양
      - 단위: px, em 등

  - border-style: 선 종류 / 기본값 none - 출력되지 않음
    - 단축 속성: margin, padding과 동일하게 방향별로 선의 종류를 지정할 수 있음
      - none: 선 없음
      - solid: 실선
      - dashed: 파선 -------------
      - dotted: 점선 ..................
      - 기타 등등

  - border-color: 선 색상 / 기본값 black
    - 단축 속성: 방향별로 선의 색상 지정 가능
      - 여러 색상
      - transparent: 투명 등
  - border-방향-속성
    - 요소의 각 방향마다 개별 테두리 스타일 적용 가능
      - `border-top: 두께 종류 색상`
      - `border-left-width: 두께;`
      - `border-right-style: 종류;`
      - `border-bottom-color: 색상;`

<h4>
    색상
</h4>

1. 색상 이름: red, tomato, royalblue, ...

   - 브라우저에서 제공하는 색상으로 브라우저마다 색상이 달라 사용 지양

2. Hex 색상 코드

   : 16진수 색상(Hexadecimal Colors) / #000, #FFFFFF, ...

   - 권장

3. RGB: r, g, b 삼원색으로 표현 / rgb(128, 0, 255), ...

4. RGBA: r, g, b + 투명도 / rgba(128, 0, 255, 0.5), ...

   - 0 <= 투명도 <= 1.

5. 기타: HSL, HSLA, ...

<h4>
    border-radius: 꼭지점 깎기
</h4>

>  요소 모서리를 둥굴게 깎아낸다.

* 속성값
  * 단위: px, em, vw 등
* 0: 깎아내지 않음. 단위 없이 표기 권장 / 기본값

> **`border-radius: 10px;`**
> 반지름 10px인 원을 요소의 두 모서리에 밀착시킨 후 원의 테두리를 따라 요소를 깎아내며,
> 정사각형 요소의 경우, 요소 크기값의 절반을 입력하면 원이 됨

* 단축 속성

  - `border-radius: 모든꼭지점속성값;`

  - `border-radius: 좌상값 우상값 우하값 좌하값;`: 좌상부터 시계방향

    ```css
    /* css */
    div {
      width: 100px;
      height: 100px;
      background-color: royalblue;
      border-radius: 10px 20px 30px 40px;
    }
    ```

<h4>
    box-sizing: 요소 가로세로 너비값 기준 설정
</h4>

>  요소의 크기 계산 기준을 지정

* 속성값

  - `content-box`: 요소의 내용으로 크기 계산 / 기본값

  - `border-box`: 요소의 내용 + padding + border

    ```css
    <!-- html -->
    <div>hello</div>
    <div>hello</div>
    /* css */
    div {
      width: 100px;
      height: 100px;
      background-color: royalblue;
      color: white;
      border: 4px solid orange;
      padding: 20px;
    }
    div:first-child {
      box-sizing: content-box;
    }
    div:nth-child(2) {
      box-sizing: border-box;
    }
    ```

<h4>
    overflow: 넘친 내용 제어
</h4>

>  요소의 크기보다 내용이 많아 넘칠때, 넘치는 내용을 어떻게 보여줄지 제어하는 단축 속성

* 속성값

  - visible: 넘친 내용 그대로 출력 / 기본값

  - hidden: 넘친 내용을 잘라냄

  - scroll: 넘친 내용만큼 잘라냄 + 넘침 여부에 관계없이 스크롤바 생성	

  - auto: 넘친 내용일 있을 경우에만 잘라내고 넘친 축에만 스크롤바 생성

    ```css
    <div class="parent">
      <div class="child">
        <div class="text">&lt;--overflow--&gt;</div>
      </div>
    </div>
    .parent {
      width: 200px;
      height: 150px;
      background-color: green;
      margin: 20px;
      overflow: visible;
    }
    .child {
      width: 300px;
      height: 100px;
      background-color: black;
    }
    .text {
      color: white;
      padding: 84px 0 0 200px;
    }
    ```

* 단축 속성

  - `overflow: xy축값;`

  - `overflow: x축값 y축값;`

* 개별 속성 : 가로, 세로 축별로 overflow 설정
  - `overflow-x`, `overflow-y`

<h4>
    display : 요소 출력 형식 제어
</h4>

> 요소마다 어떤 형식으로 화면에 출력할지 설정 - block, inline, inline-block, ...

* 속성값

  - block: 상자 요소 / div 등의 기본값

  - inline: 글자 요소 / span 등의 기본값

  - inline-block: 글자이되 상자 특성을 더함. (가로세로너비 지정 가능)

  - flex: 플렉스 박스 - 1차원 레이아웃(가로든 세로든 한 축으로 정렬)

  - grid: 그리드 - 2차원 레이아웃

  - none: 출력 특성이 없다 = 출력 안함

  - 기타 - table, table-row, table-cell, ...

    ```css
    <span>Hello world!</span>
    span {
      width: 120px;
      height: 30px;
      background-color: royalblue;
      color: white;
      display: block;
    }
    ```

<h3>
    글꼴
</h3>

<h4>
    font-style: 글자 기울기
</h4>

* 속성값

  - normal: 기울기 없음 / 기본값

  - italic: 이텔릭체

<h4>font-weight: 글자 두께</h4>

* 속성값
  - 100~900, 100단위로 9개 값
    - normal, 400: 기본값
    - bold, 700: 두껍게
    - bolder: 부모보다 두껍게
    - lighter: 부모보다 얇게

<h4>font-size: 글자 크기</h4>

* 속성값

  - 16px: 기본값

  - %, smaller 등의 상대값 키워드가 있지만 모호하므로 지양

<h4>line-height: 한 줄의 높이</h4>

* 속성값

  - normal, 1: 브라우저 기본 정의 / 기본값

  - 단위 없이 수만 입력 - 배수: 요소 글꼴 크기의 배수 ex) 1.4 ➡ 글꼴 크기의 1.4배

  - px 등의 단위도 가능하지만 배수 권장

* 지정한 높이의 중간에 줄이 정렬

  ```css
  p {
    ...
    font-size: 16px;
    font-height: 2;
  }
  ```

<h4>font-family: 글꼴 지정</h4>

* 속성값

  * 형식

    ```css
    font-family: 글꼴1, "글-꼴-2", "글 꼴 3", ..., 글꼴계열;
    ```

    - "글꼴 계열" 필수

    - "글-꼴-2", "글 꼴 3": 특수문자, 공백 포함한 글꼴명은 큰 따옴표로 묶음.

    - 글꼴1부터 차례로 사용할 수 있는 글꼴 탐색

    - 하나도 사용할 수 있는 글꼴이 없다면 글꼴 계열에서 폰트 하나 뽑아쓴다.

- 속성값
  - serif: 바탕체 계열
  - sans-serif: 고딕체 계열 / 깔끔
  - monospace: 고정 너비 계열 / 코딩
  - cursive: 필기체 계열
  - fantasy: 장식 글꼴 계열
  - 기타 등등

<h3>문자</h3>

<h4>color: 글자 색상</h4>

* 속성값

  - 위의 색상 표현 참고

  - 기본값 - rgb(0, 0, 0): 검정색

<h4>text-aling: 문자 정렬</h4>

* 속성값

  - left: 왼쪽 / 기본값

  - right, center, justify(양쪽정렬)

<h4>text-decoration: 문자에 선 추가</h4>

* 속성값

  - none: 장식 없음 / 기본값 (단, a 태그는 제외)

  - underline: 밑줄 / a 태그의 기본값

  - overline: 윗줄

  - line-through: 중앙 선

<h4>
    text-indent: 들여쓰기, 내어쓰기
</h4>

* 속성값

  * 실수값: 양수면 들여쓰기, 음수면 내어쓰기. 기본값은 0

  - 단위 - px, em, rem 등

***

<h4>
    참고할만한 내용들
</h4>
<p align="left">
    <center>
        <a href="https://developer.mozilla.org/ko/docs/Web/CSS">참조 페이지</a>
    	<img src="./Ultimate CSS Cheatsheet.png"/>&nbsp 
    </center>
</p>



