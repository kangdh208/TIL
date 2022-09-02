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

<h4>
    투명도 : opacity
</h4>

> 요소의 투명도

* 속성값
  * 0 ~ 1
    * 0 : 완전 투명
    * 1 : 불투명 / 기본값

<h4>
    글꼴
</h4>

<h5>
    font-style: 글자 기울기
</h5>


* 속성값

  - normal: 기울기 없음 / 기본값

  - italic: 이텔릭체

<h5>font-weight: 글자 두께</h5>

* 속성값
  - 100~900, 100단위로 9개 값
    - normal, 400: 기본값
    - bold, 700: 두껍게
    - bolder: 부모보다 두껍게
    - lighter: 부모보다 얇게

<h5>font-size: 글자 크기</h5>

* 속성값

  - 16px: 기본값

  - %, smaller 등의 상대값 키워드가 있지만 모호하므로 지양

<h5>line-height: 한 줄의 높이</h5>

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

<h5>font-family: 글꼴 지정</h5>

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

<h4>문자</h4>

<h5>color: 글자 색상</h5>

* 속성값

  - 위의 색상 표현 참고

  - 기본값 - rgb(0, 0, 0): 검정색

<h5>text-aling: 문자 정렬</h5>

* 속성값

  - left: 왼쪽 / 기본값

  - right, center, justify(양쪽정렬)

<h5>text-decoration: 문자에 선 추가</h5>

* 속성값

  - none: 장식 없음 / 기본값 (단, a 태그는 제외)

  - underline: 밑줄 / a 태그의 기본값

  - overline: 윗줄

  - line-through: 중앙 선

<h5>
    text-indent: 들여쓰기, 내어쓰기
</h5>


* 속성값

  * 실수값: 양수면 들여쓰기, 음수면 내어쓰기. 기본값은 0

  - 단위 - px, em, rem 등

<h4>
    배경 : Background
</h4>

<h5>
    색상 : background-color
</h5>

* 속성값
  * transparent : 투명 / 기본값

<h5>
    배경 이미지 : background-image
</h5>

* 속성값
  * none : 없음 / 기본값
  * url("이미지경로") : 이미지 경로 입력

<h5>
    배경 이미지 반복 제어 : background-repeat
</h5>

* 속성값
  * repeat : 바둑판식(반복) 배열 / 기본값
  * repeat-x / repeat-y : 각 축에만 이미지 반복 배열
  * no-repeat : 반복 안함

<h5>
    배경 이미지 위치 : background-position
</h5>

* 속성값

  * 요소 좌측 상단이 기본 위치

  * 방향: top, bottom, left, right, center

  * 단위: 요소 좌측 상단을 원점으로하여 배경 이미지 배치

    ```css
    background-position: left;`
    `background-position: bottom 10px right 20px;`
    `background-position: 25px 75px;
    ```

  * 단축속성

    * `background-position: center;`
    * `background-position: x속성값 y속성값;`

<h5>
    배경 이미지 크기 : background-size
</h5>

* 속성값
  * auto: 이미지 실제 크기 / 기본값
  * 단위: 이미지 크기 지정
  * cover: 비율 유지, 요소의 더 넓은 너비에 맞춤
  * contain: 비율 유지, 요소의 더 짧은 너비에 맞춤
  * 단축속성
    * `background-size: x크기;`: 비율 유지한채로 가로를 입력값에 맞춤
    * `background-size: x크기 y크기;`

<h5>
    배경 이미지 스크롤 특성 : background-attachment
</h5>

* 속성값
  * scroll: 배경 이미지가 요소에 고정, 스크롤시에 요소를 따라 함께 이동.
  * fixed: 배경 이미지가 뷰포트에 고정, 스크롤시에 요소를 따라 이동하지 않음.

<h4>
    배치
</h4>

<h5>
    요소 위치 설정 기준 : position
</h5>

* 속성값

  - static: 기준 없음 / 기본값

  - relative: 요소 자신 기준

  - absolute: "위치 상(?)" 부모 요소 기준

  - fixed: 뷰포트 기준

  - sticky: 스크롤 영역 기준

<h5>
    속성값들
</h5>
* 상대 속성값(relative)
  * 원래 요소의 위치를 기준으로하여 요소 배치
* 절대 속성값(absolute)
  * 위치 상 부모 요소를 기준으로 요소 배치
    * 위치 상 부모요소: position의 속성값이 static(기본값)이 아닌 가장 가까운 조상 요소
  * 다른 형제 요소들과 상호작용할 필요가 없어져 다른 요소들의 위치에 영향을 주지 않아 구조가 무너짐

* 고정 속성값(fixed)
  * 뷰포트를 기준으로 요소 배치
  * absolute와 마찬가지로 다른 형제 요소들과 상호작용하지 않게됨
  * 스크롤 이동에 관계없이 위치가 고정

1. **relative는 실제로 사용하기보다는 부모 요소에 position 속성을 선언하기에 적당**

   * absolute, fixed의 경우 다른 요소들과 상호작용을 하지 않게되며 구조가 무너지게됨
   * 구조상의 부모 요소를 위치 상의 부모 요소로 만들때도 absolute, fixed 값을 사용하면 구조가 무너지게 될 수 있으니 relative 속성값을 부여하는게 무난

2. **position 속성값이 absolute 또는 fixed인 요소는 display 속성값이 block으로 변경**

   ```html
   <!-- html -->
   <span>123</span>
   span {
     width: 100px;
     height: 100px;
     background-color: royalblue;
     color: white;
     font-size: 40px;
     position: absolute;
   }
   <!-- 출력형식 -->
   인라인 요소인 span 요소가 width, height 속성값이 적용됨 = block 요소로 출력
   ```

<h4>
    top, bottom, left, right: 요소의 방향별 거리 지정
</h4>
<h5>
    position과 함께 사용되는 속성
</h5>

* 속성값 

  * auto: 브라우저가 계산 / 기본값

  * 단위: 직접 위치 지정

    > `left: 20px;` : "왼쪽에서부터" 20px 이동 = 오른쪽으로 20px 이동

<h4>
    Stack Order : 요소 쌓임 순서
</h4>

* 어떤 요소가 더 위에 위치할지 판단하는 기준
  1. 요소에 position 속성의 값이 있는 경우 위에 쌓임. (기본값 static 제외)
  2. 1번 기준에서 같을 경우 z-index 속성의 값이 높을수록 위에 쌓임
  3. 2번 기준에서도 같을 경우 HTML의 다음 구조일 수록 위에 쌓임

> ex) 겹쳐진 두 요소가 모두 position 속성이 선언되었다면 z-index가 높은 요소가 위에 위치
>
> ex) 겹쳐진 두 요소 중 첫번째 요소만 position 속성이 선언되었다면 position 속성이 없는 두번째 요소는 첫번째 요소보다 z-index 속성값이 높던, html에서 나중에 선언되었던 첫번째 요소의 위에 위치할 수 없음
>
> ex) 겹쳐진 두 요소 모두 postion 속성값이 선언되지 않았다면 z-index 속성값을 html 구조상의 순서를 따지며 z-index 속성값도 같은 경우 html 구조상의 순서를 따짐

<h5>
    z-index : 요소의 쌓임 정도 지정
</h5> 

* 속성값

  - auto: 부모 요소와 동일한 쌓임 정도 / 기본값

  - 수: 높은 수일수록 위에 쌓임. 음수도 가능하지만 -1 정도만 사용


<h4>
    Flex : 플렉스 정렬
</h4>

> 1차원 레이아웃 : 수직, 수평

<h5>
    Flex Container & Flex Item
</h5>

* ```css
  display: flex;
  ```

  * display 속성값이 flex인 요소를 flex container
  * flex container의 자식 요소들은 flex item

> 아래에서 FC는 container에 선언하는 속성, FI는 Item에 선언하는 속성임을 표시

<h5>
    FC / display - 2
</h5>

* 속성값

  - flex: 블록 요소 특성 부여 + flex container 정의

  - inline-flex: 인라인 요소 특성 부여 + flex container 정의

    ```css
    <!-- html -->
    <span>1</span>
    <span>2</span>
    <span>3</span>
    /* css */
    span {
      background-color: greenyellow;
      display: flex;
      margin: 4px;
    }
    <!-- span 요소지만 display: flex;: 블록 요소 특성 획득, 세로로 배치됨 -->
    ```

    ```css
    <!-- html -->
    <div>hahaha</div>
    <div>hohoho</div>
    <div>hehehe</div>
    /* css */
    div {
      background-color: royalblue;
      border: 4px solid green;
      display: inline-flex;
    }
    <!-- div 요소지만 display: inline-flex;: 인라인 요소 특성, 가로로 배치됨 -->
    ```


<h5>
    FC / flex-direction: 정렬의 축을 설정
</h5>

* 속성값

  * flex container에 선언
  * flex item 정렬 축, 순서 정의

  - row: 행. 좌에서 우 / 기본값

  - row-reverse: 행. 우에서 좌

  - column: 열. 위에서 아래

  - column-reverse: 열. 아래에서 위


* `flex-direction: row;`
  * flex는 주로 수평 정렬에 사용

<h5>
    FC / flex-wrap: flex items 묶음(줄바꿈) 여부
</h5>

* 속성값

  - nowrap: 묶음 없음 / 기본값

    ```css
    .container {
      width: 400px;
      height: 200px;
      background-color: royalblue;
      display: flex;
    }
    .container .item {
      width: 100px;
      height: 100px;
      background-color: greenyellow;
      border: 4px dashed green;
    }
    ```

    - 한줄에 모두 표현하여 width, height가 100px인 박스들이 찌그러짐


  - wrap: 여러줄로 묶음
    - 한줄에 표현할 때 부모 요소를 벗어나는 요소가 생기면 줄바꿈


  - wrap-reverse: wrap의 반대 방향으로 묶음


<h5>
    FC / justify-content: 주 축의 item 정렬 방법
</h5>

* 속성값

  * flex-start: flex items를 시작점에서부터 배치 시작 / 기본값

  * flex-end: flex items를 끝점에서부터 배치 시작

  * center: flex items 가운데 정렬

  * space-between: flex items 사이를 균일하게 정렬

  * space-around: flex items의 외부 여백을 균일하게 정렬

<h5>
    FC / align-content: 교차 축의 여러 행 정렬 방법
</h5>

* 속성값
  * stretch: flex items를 시작점에서부터 배치 시작행의 높이를 늘림/ 기본값
  * flex item의 height를 지정하지 않으면 늘어나버림
  * flex-start : stretch와는 다르게 heigth를 지정하지 않아도 늘어나지 않음
  * 그 외 : center, space-between, space-around
  * flex-end 

<h5>
    FC / align-items: 교차 축의 각 행의 item 정렬 방법
</h5>

* 속성값
  - stretch: flex items를 교차 축으로 늘림 / 기본값
    - `align-content: stretch;`와 동일


- flex-start, flex-end, center
  - baseline: flex items를 각 의 문자 기준선에 정렬
  - 행의 높이는 동일하고 각 행 내에서의 item의 정렬에 관여

* 여러 줄을 제어할때는 align-content, 한 줄을 제어할때는 align-items 사용

* 한 줄 내에서 주 축 배치: justify-content / 교차 축 배치: aling-items

  ```css
  .container {
    ...
    display: flex;
    justify-content: center;
    align-items: center;
  }
  ```

<h5>
    FI / order: flex item의 정렬 순서
</h5>

* 속성값

  - 0: 순서 없음 / 기본값

  - 수: 낮은 수일수록 우선 배치

    >html의 요소 순서를 바꾸지 않고도 요소의 배치 순서를 변경 가능


<h5>
    FI / flex-grow: flex item이 여백을 차지하는 비의 항
</h5>

* 속성값

  - 0: 증가 없음 / 기본값

  - 수: 여백을 차지하는 비의 항

    > flex item 배치 후 남은 공간을 각 item들이 flex-grow값에 비례하여 나눠 갖음

<h5>
    FI / flex-shrink: flex item이 내놓는 공간의 비의 항
</h5>

* 속성값

  - 1: flex container 너비에 따라 감소 비율 적용 / 기본값

  - 수: 감소 비율. 0이면 item 크기가 변하지 않는다.

    >  공간이 부족하여 flex item이 작아져야할때 각 item들은 flex-shrink값에 비례하여 크기를 감소시킴


<h5>
    FI / flex-basis: item 공간 배분 전 기본 너비
</h5>

>  flex container의 여백 분배시에 item 자체의 크기를 특정한 값으로 덮어씌우기 가능

* 속성값

  - auto: 요소의 내용 너비

  - 단위: px, em, rem 등\

  - 예시

    - `flex-basis: auto;`
      - item의 크기 = 요소 내용의 크기 또는 지정한 크기
      - border 속성 사용 유무에 따라 box-sizing 속성값에 따라서 요소 내용의 크기가 달라지거나 테두리를 포함한 요소 자체의 크기가 달라지므로 결과 달라짐


    - `flex-basis: 0;`
      - 여백을 계산할때 item의 크기가 0으로 취급됨
    - `flex-basis: 100px;`
      - item의 크기가 어떻던간에 100px로 취급한다.


<h4>
    전환 : transition
</h4>

> 요소가 가상 클래스를 통해 전상태와 후상태를 오고갈때 자연스럽게 변화하도록 하는 효과

<h5>
    전환 효과를 지정하는 단축 속성
</h5>

* `transition: 속성명 지속시간 타이밍함수 대기시간;`: **지속시간 필수**

  ```css
  div {
    width: 100px;
    height: 100px;
    background-color: royalblue;
    transition:
      width 10s, /* 여러 속성에 다른 전환 효과 부여 가능 */
      height 5s,
      background-color 2s;
  }
  ```

* 개별속성

  - transition-property

  - transition-duration

  - transition-timing-function

  - transition-delay


<h5>
    transition-property: 전환 효과를 사용할 속성 이름 지정
</h5>

* 속성값

  - all: 모든 속성에 사용 / 기본값

  - 속성이름: 특정 속성에만 사용
    - `trainsition-property: width;`: 가로너비의 변화에만 전환 효과가 적용됨.


<h5>
    transition-duration: 전환 효과의 지속시간
</h5>

* 속성값

  - 0s: 전환 효과 없음 / 기본값

  - 시간


<h5>
    transition-timing-function: 전환 효과의 타이밍(Easing) 함수 지정
</h5>

> easing 함수: 시간에 따른 전환의 진행 정도를 표현하는 함수

* 속성값

  - ease: 느리게-빠르게-느리게 / 기본값

  - linear: 일정

  - ease-in: 느리게-빠르게

  - ease-out: 빠르게-느리게

  - ease-in-out: 느리게-빠르게-느리게

  - cubic-bezier(n,n,n,n): 사용자 정의

  - steps(n): n번 분할된 애니메이션


<h5>
    transition-delay: 전환 효과 시작까지 대기시간 지정
</h5>

* 속성값

  - 0s: 대기시간 없음 / 기본값

  - 시간
    -  `transition: 1s .5s;`
    - 전환 효과가 1초동안 지속되고 0.5초의 delay를 가진다.


<h4>
    변환 : transform
</h4>

> 요소의 변환을 정의

```css
transform: 변환함수1 변홤하수2 변환함수3 ... ;
transform: 원근법 이동 크기 회전 기울임;
```

<h5>
    변환함수
</h5>

- 2D 변환함수
  - translate(x, y): 이동 / px 단위
    - translateX, translateY
  - scale(multiple): 크기 변경 / 배수
    - scale(x, y)
    - scaleX, scaleY
  - rotate(degree): 회전 / 각도(deg)
  - skewX(x), skewY(y): 기울임 / 각도(deg)
    - skew(x, y)
  - matrix(n, n, n, n, n, n): 2차원 변환 효과 / 위의 함수들은 matrix의 여러 경우들
- 3D 변환함수
  - perspective(n): 원근법
  - translate3d(x, y, z), translateZ(z): 3d 이동
  - scale3d(x, y, z), scaleZ(z): 크기
  - rotate3d(x, y, z, a), rotateX(x), rotateY(y), rotateZ(z): 회전 (축 회전)
  - matrix3d(n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n)

<h5>
    rotate, rotateX, rotateY
</h5>

- rotate(deg): 요소 중심을 축으로하여 회전
- rotateX(deg) / rotateY(deg): X축 / Y축을 중심으로 회전. 원근법이 적용되지않은 상태

<h5>
    perspective
</h5>

```css
transform: perspective(500px) rotateX(45deg);
```

- perspective는 가장 앞에 위치
- 인수는 요소를 얼마나 먼 거리에서 바라볼 것인지 의미(요소의 중심 기준). 인수가 작을수록 큰 왜곡

<h5>
    skewX, skewY
</h5>

- 마주보는 두 모서리를 모서리와 평행하되 서로 반대인 방향으로 밀어버리는 느낌

<h4>
    perspective: 하위 요소를 바라보는 원근 거리 지정
</h4>

>  **transform 속성의 함수가 아니라 속성으로서의 perspective**

* 속성값
  - 단위: px 등 / 원근 거리
  - **perspective 속성 vs perspective 함수**


- | 분류 | 예제                                       | 적용 대상        | 기준점 설정        |
  | ---- | ------------------------------------------ | ---------------- | ------------------ |
  | 속성 | **`perspective: 600px;`**                  | 관찰 대상의 부모 | perspective-origin |
  | 함수 | **`transform: perspective(600px), ... ;`** | 관찰 대상        | transform-origin   |

- 기준점 설정 - 요소 변환의 기준점을 설정하는 기능
  
- 함수: 요소의 transform 속성에 추가 ; 바라보는 대상과 변환 대상이 같음

- 속성: 요소의 부모 요소에 선언           ; 바라보는 대상과 변환 대상이 다름

<h5>
	backface-visibility: 3D 변환된 요소의 뒷면 표시 여부    
</h5>

>  rotateX, rotateY를 180도 이상 적용했을때 뒷면을 어떻게 처리할지 정의

* 속성값

  - visible: 뒷면 표시함 / 기본값

  - hidden: 뒷면 숨김


***

<h4>
    참고할만한 내용들
</h4>
<p align="left">
    <center>
        <a href="https://developer.mozilla.org/ko/docs/Web/CSS">참조 페이지1</a>
        <a href="https://velog.io/@canlion/CSS-%EC%86%8D%EC%84%B1">참조 페이지2</a>
    	<img src="./Ultimate CSS Cheatsheet.png"/>&nbsp 
    </center>
</p>


