<h1>
    Django
</h1>
<h2>Django CRUD</h2>

> Create Read Update Delete
>

* 
  * 프로젝트
    * collection of apps
    * 프로젝트는 앱의 집합
    * 프로젝트에는 여러 앱이 포함될 수 있음
    * 앱은 여러 프로젝트에 있을 수 있음
  * 어플리케이션
    * 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할을 담당
    * 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장함

<h3>
    Django 프로젝트 파일 구조
</h3>

<h4>
    __init__.py
</h4>

* python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
* 별도의 추가 코드 작성 X

<h4>
    asgi.py
</h4>

* Asynchronous Server Gateway Interface
* Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
* 추후 배포 시 사용

<h4>
    settings.py
</h4>

* Django 프로젝트의 설정을 관리
* **프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 반드시 추가해야 함**
  * INSTALLED_APPS : Django Installation에 활성화된 모든 앱을 지정하는 문자열 목록

<h4>
    urls.py
</h4>

* 사이트의 url과 적절한 views의 연결을 지정

<h4>
    wsgi.py
</h4>

* Web Server Gateway Interface
* Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
* 추후 배포 시에 사용

<h4>
    manage.py
</h4>

* Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드 라인 유틸리티

<h3>
    Django Application
</h3>

> 생성

```bash
$ python manage.py startapp [애플리케이션 이름]

// 일반적으로 이름은 복수형으로 작성함을 권장
```

<h4>
    admin.py
</h4>

* 관리자용 페이지를 설정

<h4>
    apps.py
</h4>

* 앱의 정보가 작성된 곳
* 별도의 추가 코드 작성 X

<h4>
    models.py
</h4>

* 애플리케이션에서 사용하는 Model을 정의
* MTV패턴의 "M"

<h4>
    tests.py
</h4>

* 프로젝트의 테스트 코드를 작성

<h4>
    views.py
</h4>

* view 함수들이 정의되는 곳
* MTV패턴의 "V"

<h3>Requests && Responds</h3>

> 프로젝트 생성 후에는 실제 파일 만들기

* PJT 폴더 / urls.py 에 경로 추가
* app 폴더 / views.py 에 프로젝트 소스코드 추가

* templates 폴더 생성후 하위에 html 파일 생성

<h4>
    urls.py 경로 추가
</h4>

```python
from django.contrib import admin
from django.urls import path
from appnames import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```

<h4>
    views.py 요청을 수신/반환하는 http 함수 작성
</h4>

```python
# appnames/views.py

def index(request):
    context {
        'name' : 'name',
    }
    
    return render(request, 'index.html', context)
# context 없다면 return 에서도 생략
```

<h4>
    Templates폴더에 html 생성
</h4>

```html
<!DOCTYPE html>
<html lang='ko'>
    <head>
        <!-- 생략 -->
    </head>
    <body>
        <h1>
            Hello, World!
        </h1>
    </body>
</html>
```

* 실제 내용을 보여주는데 사용되는 파일
* 파일의 구조나 레이아웃을 정의
* Template 파일의 기본 경로
  * app 폴더 안의 templates 폴더
  * app_name/templates/
* **템플릿 폴더 이름은 반드시 templates라고 지정해야 함**

> 정리!

* Django의 코드 작성은 URL -> View -> Template 순으로 작성

* 데이터의 흐름순서
  * URL
    * path('index/', **view.index**)                     의 view.index가 
  * View
    * def ***index(request)***:                                     view 파일의 함수로
    * ​       return render(request, **'index.html'**) 의 index.html이
  * Template
    * appnames/templates/***index.html***           index.html 파일로

<h3>
    DTL
</h3>

* Django template에서 사용하는 built-in template system
* 조건, 반복, 변수 치환, 필터 등의 기능을 제공
  * Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이것은 Python 코드로 실행되는 것이 아님
  * Django 템플릿 시스템은 단순히 Python이 HTML에 포함 된 것이 아니니 주의
* 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것

<h4>
    Variable
</h4>

* {{  variable  }}
*  변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성될 수 있으나 밑줄로는 시작 할 수 없음
  * 공백이나 구두점 문자 또한 사용할 수 없음 
* dot(.)를 사용하여 변수 속성에 접근할 수 있음
* render()의 세번째 인자로 {'key': value} 와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨

<h4>
    Filters
</h4>

* {{  variable|filter  }}
* 표시할 변수를 수정할 때 사용
* 예시) {{  name|lower  }}
  * name 변수를 모두 소문자로 출력
* 60개의 built-in template filters를 제공
* chained가 가능하며 일부 필터는 인자를 받기도 함
  * {{  name|truncatewords:30  }}

<h4>
    Comments
</h4>

* {#  #}

* Django template에서 라인의 주석을 표현하기 위해 사용

* 한 줄 주석에만 사용할 수 있음 (줄 바꿈이 허용되지 않음)

* 여러 줄 주석은 {% comment %}와 {% endcomment %} 사이에 입력

  * {%  comment  %}

    여러줄

    주석

    {%  endcomment  %}















