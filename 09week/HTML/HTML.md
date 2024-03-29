<h1>
    HTML
</h1>

<h2>
    Web Programming
</h2>

* 웹프로그래밍
  * 프로그래밍 : 사람이 원하는대로 컴퓨터가 작동할 수 있도록 컴퓨터 언어로 명령어를 나열하는 행위
  * 웹 프로그래밍 : ‘웹 브라우저’와 관련된 프로그램을 작성하는 것
    * 백엔드 (back-end) 프로그래밍 : 서버에서 데이터 관리를 프로그래밍 
    * 프론트엔드(front-end) 프로그래밍 : 서버에서 받아온 정보를 웹 브라우저에 어떻게 표시할 것인지 프로그래밍

***

<h2>
    HTML
</h2>

> HyperText Markup Language
>
> 웹 페이지 및 해당 콘텐츠의 구조를 만드는 데 사용되는 코드

<h3>
    기본 구조 태그
</h3>

* !DOCTYPE
  1. 마크업 언어용 DTD 태그
  2. HTML5의 경우 맨 위에 `<!DOCTYPE html>`라고 작성하면 됨
* html
  1. 위의 DTD를 제외한 전체를 이 태그로 둘러쌈
* head
  1. HTML 문서의 속성을 지정하기 위한 태그
  2. 이 태그 안에 타이틀이나 메타 태그 등을 삽입
* body
  1. HTML 문서의 본 모양을 나타내기 위한 태그
  2. 표시될 문서의 레이아웃을 이 태그 안에 넣으면 됨

- title
  1. HTML의 제목을 선언하는 태그
- meta
  1. HTML의 부가 정보를 선언하는 태그
  2. 예를 들어 charset 속성을 쓰면 인코딩을 선언할 수 있음
- link
  1. 별도의 CSS 선언 파일, 파비콘 등을 연결하는 태그

<h3>
    레이아웃 태그
</h3>

레이아웃 태그

* 머리글 : header태그
  1. 일반적으로 페이지나 해당 섹션의 가장 윗부분에 위치
  2. 페이지 맨 위에 쓸 때는 사이트의 제목이 보통 들어가며, 선택적으로 상단바나 검색창 등이 안에 들어갈 수 있음
  3. `<head>` 태그랑 **헷갈림 주의**
  4. section이나 article, aside 등으로 묶어놓은 섹션 안의 헤더 용도로 사용가능
  
  ```html
  <header>
    <h1>Guide to Search Engines</h1>
  </header>
  ```

* nav 태그
  
  1. 내비게이션(**nav**igation)의 약자로, 일반적으로 상단바 등 사이트를 안내하는 요소에 사용
  
  2. 보통은 안에 `<ul>`을 넣어 목록 형태로 사용한다.
  
     ```html
     <nav>
       <ul>
         <li><a href="#">Home</a></li>
         <li><a href="#">Blog</a></li>
         <li><a href="#">Contact</a></li>
       </ul>
     </nav>
     ```

* main 태그

  1. 문서의 주된 콘텐츠를 표시 
  2. 이 태그는 두 개 이상 보여져서는 안 됨. 두 개 이상의 main 요소를 쓸 경우 하나 이외의 전부를 hidden 속성을 써서 가려야 함
  3. 시맨틱 태그 중에서는 `Internet Explorer`에서 유일하게 지원되지 않는 태그

* article 태그

  1. 웹 페이지의 내용에 사용하는 태그

  2. 문서나 페이지, 사이트에서 독립적으로 배포 혹은 재사용할 수 있는 섹션에 사용

     ```html
     <article>
       <h3>Google Chrome</h3>
       <p>Google Chrome is a web browser developed by Google, released in 2008. Chrome is the world's most popular web browser today!</p>
     </article>
     ```

* section 태그

  1. 웹 페이지의 섹션에 사용하는 태그, 웹 페이지를 의미적으로 각각의 파트로 구분하기 위해 쓰는 태그

     ```html
     <section>
       <h2>Internet Browsers</h2>
       <p>Google Chrome, Mozilla Firefox, Internet Explorer, Safari and Opera dominate the browser market.</p>
     </section>
     ```

* aside 태그

  1. 본문의 주요 부분을 표시하고 남은 부분을 설명하는 태그

  2. 특별한 일이 아니면 사이드바나 광고창 등 중요하지 않은 부분에 사용

     ```html
     <p>Google Chrome is a cross-platform web browser developed by Google.</p>
     
     <aside>
       <h4>History of Mozilla</h4>
       <p>Mozilla is a free software community founded in 1998.</p>
     </aside>
     ```

* footer

  1. 일반적으로 페이지나 해당 파트의 가장 아랫부분에 위치

  2. 페이지 맨 아래에 쓸 때는 사이트의 라이선스, 주소, 연락처 등을 넣는다.

     ```html
     <footer>
       <p>Copyright Example.com. Read our <a href="#">privacy policy</a>.</p>
     </footer>
     ```

<h3>
    텍스트 관련
</h3>

* `<h[1-6]>`

  1. 제목(heading)을 표시할 때 사용 

  2. `<h1>`이 가장 크고 `<h6>`이 가장 작으며 크기는 브라우저마다 표시하는 방법이 달라 다를 수 있음

  3. CSS를 쓰면 크기, 색상, 폰트 등을 변경할 수 있음 

  4. `<h1>`은 한 문서 안에 하나만 사용하는 것을 권장

     ```html
     <h1>1단계</h1>
     <h2>2단계</h2>
     <h3>3단계</h3>
     <h4>4단계</h4>
     <h5>5단계</h5>
     <h6>6단계</h6>
     ```

     `<p>`: 새 문단(

- `<p>`

  1. 새 문단(paragraph)을 열고 `</p>`로 닫음

  2. 이 태그를 쓸 경우 기본적으로 문단 하단에 약 1줄 가량의 빈 공간이 생기기 때문에 `<br>`을 선호하는 경우가 많은데, 문단이라면 `<p>` 태그로 묶어주는 것이 올바른 사용법

  3. 빈 공간은 CSS를 지정해서 없앨 수 있음

     ```html
     <p>이 밑에 빈 공간이 있습니다.</p>
     <p>이 위에 빈 공간이 있습니다.</p>
     
     이 밑에 빈 공간이 있습니다.
     (빈 공간)
     이 위에 빈 공간이 있습니다.
     ```

- `<b>`

  1. 두껍게(bold) 효과
  2. 강조의 의미를 줄 때는 `<strong>` 태그로 대체하고 그 이외에는 CSS의 `font-weight: bold;` 속성으로 쓸 것을 권장하고 있었지만 HTML5에서 `<strong>`보다 약한 의미의 강조로 다시 복귀

- `<i>`

  1. 텍스트를 기울임꼴(italic)
  2. 표시기술 용어, 외국어, 일반적으로 기울임꼴로 사용되는 용어 등을 강조

- `<strong>`

  1. 포함된 텍스트를 강하게 강조할 때 사용

- `<em>` 

  1. `<strong>`보다 약한 강조를 나타낼 때 사용

     ```html
     <b>굵게 표시됩니다.</b>
     <i>기울임꼴로 표시됩니다.</i>
     <strong>강하게 강조합니다.</strong>
     <em>약하게 강조합니다.</em>
     ```

     > <b>굵게 표시됩니다.</b>
     > <i>기울임꼴로 표시됩니다.</i>
     > <strong>강하게 강조합니다.</strong>
     > <em>약하게 강조합니다.</em>

- `<ins>`

  1. 문서에 삽입(insert)된 텍스트, 즉 밑줄을 표시

- `<del>`

  1. 문서에서 삭제(delete)된 텍스트, 즉 취소선을 표시

- `<s>`

  1. 취소선(strikethough)을 표시
  2. HTML 4.01에서 비권장 태그로 되었다가 HTML5에서 `<del>`보다는 약한 삭제의 의미로 변경되면서 존치

- `<u>`

  1. 밑줄(underline)을 표시

  2. 주로 철자 오류를 지적하는 데 사용

     ```html
     <ins>밑줄이 표시됩니다.</ins>
     <del>취소선이 표시됩니다.</del>
     <s>역시 취소선입니다.</s>
     <u>밑줄이 표시됐습니다.</u>
     ```

     > 밑줄이 표시됩니다.
     > ~~취소선이 표시됩니다.~~
     > ~~역시 취소선입니다.~~
     > 밑줄이 표시됐습니다.

- `<sup>`

  1. 텍스트를 위첨자(superscript)로 표시

- `<sub>`

  1. 텍스트를 아래첨자(subscript)로 표시

     ```html
     E=MC<sup>2</sup>
     H<sub>2</sub>O는 산소가 아닌 물입니다.
     YP<sub>B</sub>P<sub>R</sub>
     ```

- `<small>`

  1. 텍스트를 조금 더 작게 표시
  2. `<big>` 태그가 HTML5 규격에서 제외된 것과는 달리 `<small>` 태그는 존치
  3. 주로 저작권 정보나 주석을 조그맣게 다는 데 사용

  ```html
  <small>작은글자</small>
  ```

- `<br>`

  1. 문단 내 줄바꿈(line break).
  2. 강제개행을 하는 태그
  3. 문단의 흐름을 해치기 때문에 권장되는 태그는 아님

- `<hr>`

  1. 가로줄(horizontal rule)을 삽입

     ```html
     이 밑에 가로줄이 있습니다.
     <hr>
     이 위에 가로줄이 있습니다.
     ```

- `<abbr>`

  1. 약어를 이 태그로 묶어서 무엇의 약어인지 설명하기 위한 태그
  2. `<abbr title="약어에 대한 설명">약어</abbr>` 식으로 써서 마우스 커서를 대면 설명이 나와 읽을 수 있음
  3. 원래는 특별한 시각적 효과를 부여하려면 CSS를 사용해야 했지만 구글 크롬과 파이어폭스에서는 언제부터인가 CSS를 지정하지 않더라도 자동으로 점선 밑줄이 생김

- `<wbr>`

  1. 글이 길어질 때 띄어쓰기가 없더라도 이 태그가 쓰인 부분에서 자동개행이 이루어짐
  2. 원래는 개행을 방지하는 비표준 태그 `<nobr>` 안애서 `<br>` 태그와 같은 기능을 하는 태그였으나 HTML5에서 표준으로 채택되면서 기능이 변경된 것
  3. 다만 한글은 글자 단위로 개행이 되기 때문에 한글에다가 이 태그를 쓸 필요성은 거의 없음

- `<blockquote>`

  1. 인용구를 기술하는 태그
  2. 기본적으로 들여쓰기가 되어 있는데 CSS로 제거 가능

- `<q>`

  1. `<blockquote>`의 인라인 버전

- `<dfn>`

  1. `<dl>`의 인라인 버전

- `<pre>`

  1. 서식 있는(Preformatted) 텍스트를 넣기 위한 태그
  2. 이 태그 안에는 `<br>` 태그 없이 개행하더라도 개행을 인식하고 공백 문자가 두 개 이상 연속으로 있어도 하나로 취급하지 않고 그대로 표시
  3. 또한, 일반적으로 이 태그 안에 들어간 텍스트는 고정폭 글꼴로 표시
  4. 이 태그 안에 다른 태그를 넣으면 경우에 따라 의도치 않게 표시될 수도 있으므로 가급적이면 다른 태그를 넣지 않는 것을 권장

- `<var>`, `<samp>`, `<kbd>`, `<code>`

  1. 변수 등 프로그래밍 언어와의 연계를 위한 태그

- `<ruby>`

  - 후리가나(일본어 한자 위에 적히는 독음표기) 표기에 쓰이는 기본 태그

    - `<rp>`: 후리가나가 지원되지 않는 환경에서 표기할 텍스트를 지정한다.
    - `<rt>`: 후리가나를 작성

    ```html
    <ruby>漢字<rp>(</rp><rt>かんじ</rt><rp>)</rp></ruby>
    ```

<h3>
    목록 태그
</h3>

- `<ul>`

  1. 순서 없는 목록(unordered list)을 표시한다.

- `<li>`

  1. 목록에서 각 항목(list item)은 `<li>`와 `</li>`사이에 삽입

  2. `<li>`와 `</li>`사이에 또 목록을 넣으면 하위 목록도 가능

     ```html
     <ul>
     　　<li>순서가 없는 첫번째 항목입니다.</li>
     　　<li>순서가 없는 두번째 항목입니다.</li>
     </ul>
     
     <ul>
     　　<li>첫 번째</li>
     　　<li>두 번째
     　　　　<ul>
     　　　　　　<li>두 번째 속 첫 번째</li>
     　　　　　　<li>두 번째 속 두 번째</li>
     　　　　</ul>
     　　</li>
     </ul>
     ```

- `<ol>`

  1. 순서 있는 목록(ordered list)을 표시

  2. `<ul>` 안에 하위 목록으로 `<ol>`을 넣을 수도 있으며, 반대로 `<ol>` 안에 하위 목록으로 `<ul>`을 넣는 것도 가능

     ```html
     <ol>
     　　<li>순서가 있는 첫번째 항목입니다.</li>
     　　<li>순서가 있는 두번째 항목입니다.</li>
     </ol>
     
     <ul>
     　　<li>가나다</li>
     　　<li>라마바
     　　　　<ol>
     　　　　　　<li>사아자</li>
     　　　　　　<li>차카타</li>
     　　　　</ol>
     　　</li>
     　　<li>파하</li>
     </ul>
     ```

- `<dl>`
  1. 정의 목록(definition list)을 표시
- `<dt>`
  1. 정의 목록의 정의(definition term)를 기술
- `<dd>`
  1. 정의 목록의 뜻풀이(definition description)를 기술
  2. 기본적으로 들여쓰기가 되어 있는데 CSS 로 제거가능

<h3>
    링크, 멀티미디어 태그
</h3>

* `<a>`
  1. 하이퍼링크를 생성하는 태그
  2. Anchor의 줄임말
  3. href 속성을 써서 `<a href="링크할 페이지">내용</a>`와 같이 작성
  4. `<a>`태그는 겹쳐서 `<a> <a> </a> </a>`로 작성 불가 **주의**
* `<img>`
  1. 페이지에 이미지를 추가하는 태그이다.
     * src: source의 약자로 이미지파일의 경로를 지정하는 태그 속성
     * http:// 또는 https://: 절대경로 URL로 지정
     * path/to/image/file: 상대경로로 지정
     * data:image/jpeg|png|gif;base64, A1bC2dE3fG...: 파일을 base64로 인코딩한 형태로 지정
       * 작은 여러 개의 파일이 있을 경우 권장하며, 큰 파일은 절대 권장하지 않음
     * alt: 이미지를 볼 수 없는 경우에 이미지에 대한 설명을 제공
       * 이 속성값이 없어도 파일의 경로가 유효하다면 표시되기는 하지만 웹표준 검사기에서 걸림
     * title: 이미지에 대한 추가 정보를 제공
     * height, width: 이미지의 세로, 가로폭을 지정
       * HTML 4.01까지는 그냥 숫자만 쓰면 픽셀로, 뒤에 %를 붙이면 백분율로 지정할 수 있었으나, HTML5에서는 픽셀로만 지정할 수 있게 되었으므로 백분율로 지정하려면 CSS를 사용해야함

* `<svg>`
  1. 페이지에 SVG 형식의 그래픽을 추가하는 태그
  2. SVG 파일은 위의 `<img>` 태그로 넣어도 되지만 SVG 파일이 XML형식으로 만들어져 있기에 별도의 SVG 파일을 만들지 않고 직접 코딩해서 넣는 것도 가능하며 이 때 `<svg>` 태그를 사용
* `<progress>`
  1. 페이지에 진행 상황 막대를 추가하는 태그
  2. 예를 들어 `<progress value="22" max="100"></progress>`와 같이 쓸 경우 22% 진행된 막대가 표시

- `<audio>`
  1. 음성, 음악 파일 등을 재생할 수 있는 태그
  2. 웹 브라우저마다 지원하는 확장자가 달라 멀티브라우저 지원을 위해서는 `<source>` 태그를 안에 넣어서 두가지 이상의 확장자를 가진 음악 파일을 넣어야 함
  3. 가장 많이 사용하는 조합은 mp3 + ogg
- `<video>`
  1. 영상 파일을 재생할 수 있는 태그
  2. 별다른 플러그인 없이도 자체 재생이 가능하다는 점이 가장 큰 장점
  3. `<audio>` 태그와 마찬가지로 `<source>` 태그를 넣어 mp4 + ogv의 조합으로 짜주면 거의 대부분의 브라우저를 지원
- `<canvas>`
  1. 스크립트를 이용하여 그래픽을 표현하는 태그
  2. 일반적으로는 JavaScript를 많이 사용하며, 응용하면 웹에서 게임 앱, 3D 엔진 등을 돌리는 다양한 응용이 가능

<h3>
    그 외 태그들
</h3>

* `<style>`
  1. CSS 사용
  2. 되도록이면 `<link>` 태그를 쓰기를 권장
* `<script>`
  1. 스크립트를 사용 
  2. `<script type="text/javascript">` ... `</script>` 식으로 스크립트 타입을 지정해서 사용
  3. HTML5에서는 type 속성을 생략하면 일반적으로 사용되는 자바스크립트로 인식
* `<div>`
  1. 박스 또는 레이어
  2. 일명 '웹 표준' 개념이 많은 사람들에게 퍼지게 된 이후 테이블 태그 대신 레이아웃을 만드는 데 자주 사용되고 있음
  3. `<div>` 이외에도 많은 태그가 `<div>`와 같은 박스 스타일로 렌더링되기 때문에 CSS를 잘 지정해 사용

<h3>
    HTML 문서 구조화
</h3>

- table의 각 영역을 명시하기 위해 <thead>, <tbody>, <tfoot> 요소를 활용

- 테이블 태그에 3요소가 모두 필요한 것은 아니다. 선택해서 활용하면 된다.

- <tr>로 가로 줄을 구성하고 내부에는 <th> 혹은 <td> 로 셀을 구성

- colspan, rowspan을 통해 셀 병합

  ```html
  <body>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Major</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>홍길동</td>
          <td>Computer Science</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <td>총계</td>
          <td colspan="2">1명</td>
      </tfoot>
      <caption>학생 명단</caption>
    </table>
  </body>
  ```

<h3>
    Form
</h3>

> [Form Reference](https://web.dev/learn/forms/)

- `<form>`은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그

- <form> 기본 속성

  - action: form을 처리할 서버의 URL(데이터를 보낼 곳)

  - method: form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)

  - enctype: method가 post인 경우 데이터의 유형

    - application/x-www-form-urlencoded: 기본값
    - mulitpart/form-data: 파일 전송시(input type이 file인 경우)
    - text/plain: HTML5 디버깅 용 (잘 사용되지 않음)

    ```html
    <form action="/search" method="GET">
    </form>
    ```

<h3>
    Input
</h3>

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

- `<input>` 대표적인 속성

  - name : form control에 적용되는 이름 (이름/ 값 페어로 전송됨)

  - value : form control에 적용되는 값 (이름/값 페어로 전송됨)

  - required, readonly, autofocus, autocomplete, disabled 등

    ```html
    <form action="/search" method="GET">
      username: <input type="text" name="q">
    </form>
    >> https://www.google.com/search?q=HTML
    ```

<h4>
    Input Label
</h4>

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음

  - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일 환경에서 편하게 사용할 수 있음
  - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인 할 수 있도록 함

- `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킴

  ```html
  <label for="agreement">개인정보 수집에 동의합니다.</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```

  - 예제

    ```html
    <body>
      <form action="">
        <label for="username">username</label>
        <input type="email" name="username" id="username">
        <input for="password">password</label>
        <input type="password" name="password" id="password">
        <input type="submit" value="얍!">
      </form>
    </bdoy>
    ```

<h4>
    Input Type
</h4>

- 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
  - text : 일반 텍스트 입력
  - password : 입력 시 값이 보이지 않고 문자를 특수기호로 표현
  - email : 이메일 형식이 아닌 경우 form 제출 불가
  - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
  - file : accept 속성을 활용하여 파일 타입 지정 가능

<h5>
    Input Type - 항목 중에 선택하기
</h5>

- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함

- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야함

  - checkbox : 다중 선택

  - radio : 단일 선택

    ```html
    <div>
      <p>checkbox</p>
      <input id="html" type="checkbox" name="language" value="html">
      <label for="html">HTML</label>
      <input id="python" type="checkbox" name="language" value="python">
      <lable for="python">파이썬</label>
      <hr>
      <p>radio</p>
      <input id="html" type="radio" name="language" value="html">
      <label for="html">HTML</label>
      <input id="python" type="radio" name="language" value="python">
      <lable for="python">파이썬</label>
    </div>
    ```

<h5>
    Input Type - 그 외
</h5>

- 다양한 종류의 input을 위한 picker를 제공
  - color : color picker
  - date : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정 (django 다룰때 다시함)
  - hidden : 사용자에게 보이지 않는 input

***

<h4>
    참고할만한 내용들
</h4>

<p align="left">
    <center>
        <a href="https://developer.mozilla.org/ko/docs/Web/HTML">참조 페이지</a>
    	<img src="./Ultimate HTML Cheatsheet.png"/>&nbsp 
    </center>
</p>


