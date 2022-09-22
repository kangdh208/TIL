<h1>
    Django
</h1>
<h2>Django : Python</h2>




> 장고란 무엇인가요?
>
> Django 는 파이썬으로 만들어진 무료 오픈소스 웹 애플리케이션 프레임워크(web application framework)

> 1. 누군가가 서버에 웹 사이트를 요청 >> 장고로 전달
> 2. 장고 **`urlresolver`**는 웹 페이지의 주소를 가져와 무엇을 할지 확인
> 3. `unresolver`는 패턴 목록을 가져와 URL과 맞는지 처음부터 하나씩 대조해 식별 >> 만약 일치하는 패턴이 있으면, 장고는 해당 요청을 관련된 함수(*view*)에 넘겨줌
> 4. 



<h3>
    Django 개발환경 설정
</h3>

<h4>
    가상환경 생성/실행
</h4>

<h6>
    venv생성
</h6>

* python3는 venv 모듈이 내장

* 가상환경을 구성할 프로젝트 디렉터리에서 진행

  ```bash
  $ mkdir [project file]
  $ cd [project directory]
  $ python -m venv [가상환경 이름]
  
  $ ls             // 생성
  [가상환경 이름]    // 생성 확인 완료
  
  // 예시
  $ mkdir server
  $ cd server
  $ python -m venv .venv
  
  $ ls
  .venv
  ```

  * 버전관리시스템에 올리지 않을 때는 gitignore

    ```bash
    $ echo '가상환경이름' >> .gitignore
    ```

<h6>
    venv 활성화
</h6>

* 생성된 가상환경을 활성화 하면 `(가상환경이름)`이 bash에 생성

  ```bash
  $ source [가상환경이름]/Scripts/activate
  [가상환경이름] $
  
  // 예시
  $ source .venv/Scripts/activate
  (.venv) $
  ```

<h6>
    venv 비활성화
</h6>

* 가상 환경을 빠져나올 떄는 터밀널에 `deactivate`만 입력

  ```bash
  (.venv) $ deactivate
  $
  ```

<h6>
    가상환경 삭제
</h6>

* 디렉토리를 지우면 가상환경도 삭제

  ```bash
  $ pwd                     // 가상환경 디렉토리 확인
  ~/server
  $ rm -r [가상환경 이름]     // 삭제 명령어
  $ ls
  $                         // 삭제 확인
  ```

<h4>
    Django LTS 버전 설치
</h4>

* LTS버전 : LONG TERM SUPPORT, 장기 지원 버전

* 가상 환경이 활성화된 상태에서 패키지를 설치하면, [가상환경 이름] 디렉터리 내부에 해당 패키지가 설치

  ```bash
  // command
  (가상환경이름) $ pip install django==[장고 버전]
  ```

  ```bash
  (.venv) $ pip install django==3.2.13
  Collecting Django==3.2.13
    Downloading Django-3.2.13-py3-none-any.whl (7.1MB)
  Installing collected packages: Django
  Successfully installed Django-3.2.13
  ```

<h4>
    Django 프로젝트 생성
</h4>

* 장고에서는 디렉토리와 파일명이 매우 중요

  * 파일명을 마음대로 변경해서도 안되고 다른 곳으로 옮겨도 안됨
  * 장고는 중요한 것들을 찾을 수 있게 특정한 구조를 유지해야 함

  ```bash
  (.venv) $ django-admin startproject [projectName] .
  
  // 혹은
  
  (.venv) $ python -m django startproject [projectName] .
  ```

  * 명령 끝에 **`.`(점) 입력 필수**
  * 점은 현재 디렉토리에 장고를 설치하라고 스크립트에 알려 주는 것
  * 생성시 `manage.py`, `[projectName] 디렉토리` 가 생성
  * `manage.py`
    * 사이트 관리를 도와주는 역할을 하는 스크립트
  * `[projectName]디렉토리` 아래에 `urls.py`파일은 `urlresolver`가 사용하는 패턴 목록 포함

<h4>
    Django 실행
</h4>

local host : 8000

* project 로 이동후 장고 실행하여 장고프로젝트 실행 가능

  ```bash
  (.venv) python manage.py runserver
  Watching for file chnages with StatReloader
  Performing system checks...
  
  System check identified no issues (0 silenced).
  September 21, 2022 - 11:32:22
  Django version 3.2.13, using settings 'firstserver.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
  ```

* 웹 브라우저에서 실행도 가능

  ```web-idl
  //주소창
  
  127.0.0.1:8000
  // 혹은
  localhost:8000
  ```

* 종료 방법은 Control + C

***

<h2>
    Reference
</h2>

* [DjangoTutorial](https://tutorial.djangogirls.org/ko/)

* [JumpToPython](https://wikidocs.net/72280)

***

<h4>
    EXTRA TERM
</h4>

* IP 와 도메인
  * IP주소 : 다른 호스트와 데이터를 주고 받기 위해 자신들을 구분하는 특수한 번호
    * 4개의 숫자와 점으로 구성되어 있으며, 각각의 숫자는 0 ~ 255 사이의 정수
    * 로컬 호스트는 호스트 자기 자신을 가리키는 고유한 별칭으로 IP주소 127.0.0.1로 설정
  * 도메인은 URL(Uniform Resource Locator)의 일부
    * 넓게 보면 외우거나 식별하기 어려운 IP 주소(예:240.10.20.1)를 example.com 처럼 기억하기 쉽게 만들어주는 네트워크 호스트 이름을 의미
    *  루트 네임 서버(최상위 DNS서버) 등록된 최상위 호스트 네임 및 각 최상위 호스트 네임을 관리하는 도메인 레지스트리에서 관리하는 하위 호스트 네임을 이르는 말
  * DNS(Domain Name System, 도메인 네임 시스템)
    * 영문/한글 주소를 IP 네트워크에서 찾아갈 수 있는 IP로 변환
    * Name Server(네임 서버) : 도메인과 IP 연결 정보가 있는 서버
  * [REF](https://developer.mozilla.org/ko/docs/Learn/Common_questions/How_does_the_Internet_work)
* 클라이언트와 서버
  * Host(호스트) : 네트워크에 연결되어 있는 각각의 장치
  * 호스트가 데이터를 Request(요청)했을 때 이에 Response(응답)
  * Server(서버) : 서비스를 제공(응답)하는 쪽의 호스트
  * Client(클라이언트) : 데이터를 요청하는 쪽의 호스트
  * [REF1](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
  * [REF2](https://developer.mozilla.org/ko/docs/Learn/Common_questions/What_is_a_web_server)

* 정적 웹 사이트와 동적 웹 사이트
  * 정적 웹 사이트
    * 서버에 미리 저장된 파일이 그대로 전달되는 웹 페이지
    * 서버는 사용자의 요청에 해당하는 저장된 웹 페이지를 응답
    * 사용자는 서버에 저장된 데이터가 변경되지 않는 한 고정된 웹 페이지를 응답받음
    * 장점
      * 파일에 대한 추가작업이 없어 빠름
      * 웹서버만 구축하면 되므로 비용이 적음
    * 단점
      * 저장된 정보만 보여주므로 서비스가 한정적
      * 사이트의 구조에 따라 추가,수정,삭제등의 작업이 어려워 관리가 힘듦
  * 동적 웹 사이트
    * 서버에 있는 데이터들을 스크립트에 의해 가공처리한 후 생성되어 전달되는 웹 페이지
    * 서버는 사용자의 요청을 해석하여 데이터를 가공한 후 생성되는 웹 페이지를 보냄
    * 사용자는 상황, 시간, 요청 등에 따라 달라지는 웹 페이지를 보게 됨
    * 장점
      * 다양한 정보를 조합 후 동적으로 생성하여 제공하므로 서비스가 다양
      * 사이트의 구조에 따라 추가,수정,삭제등의 작업이 용이해서 관리가 쉬움
    * 단점
      * 사용자에게 웹 페이지 전달까지 처리하는 작업이 필요해서 상대적으로 느림
      * 웹 서버외에 추가처리가 필요한 WAS(Web Application Server, 웹어플리케이션 서버)가 필요해 추가 비용이 듬
  * [REF](https://developer.mozilla.org/ko/docs/Learn/Server-side/First_steps/Introduction)
* HTTP
  * HyperText Transfer Protocol, 문자를 전송하기 위한 프로토콜
  * 서버와 클라이언트의 사이에서 어떻게 메시지를 교환할지를 정해 놓은 규칙
  * HTTP는 FTP나 텔넷과는 다르게 비연결식
  * HTTP는 클라이언트가 서버에 정보를 요청하면 응답 코드와 내용을 전송하고 클라이언트와 연결을 종료
* 요청과 응답메시지 구성
  * 요청 메시지 종류
    * GET: 클라이언트가 서버에게 URL에 해당하는 자료의 전송을 요청
    * HEAD: GET 요청으로 반환될 데이터 중 헤더 부분에 해당하는 데이터만 요청
    * POST: 클라이언트가 서버에서 처리할 수 있는 자료를 전송, 멱등성을 보장하지 않음
    * PATCH: 클라이언트가 서버에게 지정한 URL의 데이터를 부분적으로 수정할 것을 요청
    * PUT: 클라이언트가 서버에게 지정한 URL에 지정한 데이터를 저장할 것을 요청
    * DELETE: 클라이언트가 서버에게 지정한 URL의 정보를 제거할 것을 요청
    * TRACE: 클라이언트가 서버에게 송신한 요청의 내용을 반환해 줄 것을 요청
    * CONNECT: 클라이언트가 특정 종류의 프록시 서버에게 연결을 요청
    * OPTIONS: 해당 URL에서 지원하는 요청 메세지의 목록을 요청
  * 응답 코드 종류
    * 1XX : 정보 전달, 요청을 받았고 작업을 진행 중
      * 100 Continue
      * 101 Switching Protocols
      * 102 Processing : 사용자가 수신요청을 하여 처리하고는 있지만 아직은 제대로 된 응답을 할 수 없는 상태임을 응답하는 코드
      * 103 Early Hints : 주로 서버가 응답을 준비하는 동안 사용자가 사전로딩(PreLoading)을 할 수 있도록 하는 응답코드
    * 2XX : 성공, 작업이 성공적으로 받아들여짐
      * 200 OK: 성공적으로 처리했을 때 사용
      * 201 Created: 요청이 성공적으로 처리되어서 리소스가 만들어졌음을 의미
      * 202 Accepted: 요청이 받아들여졌지만 처리되지 않았음을 의미
      * 203 Non-Authoritative Information : 응답받은 메타정보가 서버에 저장된 원본하고는 동일하지는 않지만 로컬이나 다른 복사본에서 수집되었음을 알리는 응답코드
      * 204 No Content: 성공적으로 처리했지만 컨텐츠를 제공하지는 않는 응답코드
      * 205 Reset Content: 서버가 요청을 성공적으로 처리했지만 콘텐츠를 표시하지 않는 응답코드로 204 응답과 달리 이 응답은 요청자가 문서 보기를 재설정할 것을 요구
      * 206 Partial Content: 컨텐츠의 일부 부분만 제공하는 응답코드
    * 3XX : 리다이렉션, 요청을 완료하기 위해 리다이렉션 필요
      * 301 Moved Permanently(영구 이동): 영구적으로 컨텐츠가 이동했을 때 사용
      * 302 Found: 일시적으로 컨텐츠가 이동했을때 사용
      * 303 See Other: 서버가 사용자의 GET 요청을 처리하여 다른 URL에서 요청된 정보를 가져올 수 있도록 응답하는 코드
      * 304 Not Modified: 200 다음으로 많이 볼 수 있는 HTTP 상태, 이 경우 보통 브라우저에 캐시되어 있는 버전을 사용
    * 4XX : 클라이언트 오류, 요청이 올바르지 않음
      * **400 Bad Request**(잘못된 요청): 요청 자체가 잘못되었을 때 사용하는 코드
      * **401 Unauthorized**(권한 없음): 인증이 필요한 리소스에 인증 없이 접근할 경우 발생, 이 응답 코드를 사용할 때에는 반드시 브라우저에 어느 인증 방식을 사용할 것인지 보내야 함
      * 402 Payment Required(결제 필요): 결제가 필요한 리소스에 결제없이 접근했을 경우 발생.
      * **403 Forbidden**(거부됨): 서버가 요청을 거부할 때 발생. 관리자가 해당 사용자를 차단했거나 서버에 index.html 이 없는 경우에도 발생 가능하며, 혹은 권한이 없을 때(로그인 여부와는 무관하다)에도 발생
      * **404 Not Found**(찾을 수 없음): 찾는 리소스가 없다는 뜻으로, 가장 흔하게 볼 수 있는 오류 코드
      * 405 Method Not Allowed(허용되지 않은 방법) : PUT이나 DELETE 등 서버에서 허용되지 않은 메소드로 요청시 사용하는 코드
      * 406 Not Acceptable(받아들일 수 없음) : 요청은 정상이나 서버에서 받아들일 수 없는 요청일시 사용하는 코드, 보통 웹 방화벽에 걸리는 경우 이 코드가 반환
      * 407 Proxy Authentication Required(프록시 인증 필요) : 프록시 인증이 필요할 경우 사용하는 코드
      * **408 Request Timeout**(요청 시간 초과) : 요청 중 시간이 초과되었을때 사용하는 코드
    * 5XX : 서버 오류, 서버가 응답이 불가하며 요청이 올바른지는 판단 불가
      * **500 Internal Server Error**(내부 서버 오류): 서버에 설정이나 퍼미션 문제 등의 오류가 발생해 작업을 수행할 수 없을 때 사용
      * 501 Not Implemented(요청한 기능 미지원): 서버가 요청을 수행하는데 필요한 기능을 지원하지 않는 경우 사용
      * **502 Bad Gateway**(게이트웨이 불량): 게이트웨이가 연결된 서버로부터 잘못된 응답을 받았을 때 사용
      * **503 Service Temporarily Unavailable**(일시적으로 서비스를 이용할 수 없음): 웹서버 등이 과부하로 다운되었을 때와 같이 서비스를 일시적으로 사용할 수 없을 때 사용
      * **504 Gateway Timeout**(게이트웨이 시간초과): 게이트웨이가 연결된 서버로부터 응답을 받을 수 없었을 때 사용
  * [REF](https://developer.mozilla.org/ko/docs/Web/HTTP/Overview)
* 프레임워크
  * 어떠한 목적을 달성하기 위해 복잡하게 얽혀있는 문제를 해결하기 위한 구조
  * 웹 개발을 위한 프레임워크는 웹 프레임워크/웹 어플리케이션 프레임워크
  * 여러 기능을 가진 클래스와 라이브러리가 합쳐진 형태로 재사용성을 큰 그룹 단위로 묶은 형태

| 언어/라이브러리 | 프레임워크 | 언어/라이브러리 | 프레임워크    |
| --------------- | ---------- | --------------- | ------------- |
| Python          | Django     | Java            | Spring        |
| JavaScript      | AngularJS  | Ruby            | Ruby on Rails |
| JavaScript      | React      | PHP             | Laravel       |
| JavaScript      | Vue.js     | TypeScript      | Angular       |

