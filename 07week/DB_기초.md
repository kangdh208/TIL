<h1>
DB 기초    
</h1>
<h2>DataBase</h2>

> 데이터베이스는 체계화된 데이터의 모임
>
> 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
>
> 논리적으로 연관된 하나 이상의 자료의 모음으로 그 내용을 구조화하여 검색과 갱신의 효율화를 꾀하는 것
>
> 몇개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체

<h4>
    DB의 장점
</h4>

* 데이터 중복 최소화
* 데이터 무결성 (정확한 정보를 보장)
* 데이터 일관성
* 데이터 독립성 (물리적 / 논리적)
* 데이터 표준화
* 데이터 보안 유지

<h2>
    RDB(Realtional DataBase)
</h2>

> 관계형 데이터베이스

* 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형
* 키(Key)와 값(Value)들의 간단한 관계를 표 형태로 정리한 데이터베이스

<h4>
    관련 용어
</h4>

* 스키마(Schema)
  * 데이터베이스에서 자료의 구조, 표현바법, 관계등 전반적인 명세를 기술한 것
  * 이 명세를 토대로 표(Table)을 구성

* 테이블(table)
  * 데이터 요소들의 집합
  * 열(column) : 각 열에 고유한 데이터 형식 지정
    - address라는 필드에 살고 있는 도시(TEXT) 정보가 저장
  * 행(row) : 실제 데이터가 저장되는 형태
    - 총 3명의 고객정보가 저장되어 있음 = 레코드가 3개
  * 기본키(Primary Key) : 각 행(레코드)의 고유 값
    - 반드시 설정해야 함, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨

<h3>
    RDBMS(Relational DataBase Management System)
</h3>

> 관계형 모델을 기반으로 하는 데이터베이스 관리시스템
>
> ex) MySQL, SQLite, Oracle, MariaDB 등

* SQLite
  * 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
  * 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스, 임베디드 소프트웨어에도 많이 활용
  * 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용 가능

<h3>
    SQL(Structured Query Language)
</h3>

* 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적으로 만들어진 프로그래밍 언어
* 데이터베이스 스키마 생성 및 수정
* 자료의 검색 및 관리
* 데이터베이스 객체 접근 조정 관리

<h5>
    분류
</h5>

* DDL(Data Definite Language)
  - **데이터 정의 언어**
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - CREATE, ALTER, DROP
* DML(Data Manipulation Language)
  - **데이터 조작 언어**
  - 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어
  - SELECT, INSERT, UPDATE, DELETE
* DCL(Data Control Language)/TCL(Transaction Contral Language)
  - **데이터 제어 언어**/트랜잭션제어어
  - 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
  - GRANT, REVOKE, COMMIT, ROLLBACK

<h4>
    SQL 기초 문법
</h4>

> SQLite 기준

<h5>
    기초 문법
</h5>

* 테이블 생성

  * CREATE TABLE [테이블 이름];

    ```sql
    CREATE TABLE classmates(
      id INTEGER PRIMARY KEY,
      name TEXT
    );
    ```

* 테이블 목록 조회

  * .table

    ```sql
    .tables
    
    classmates
    ```

* 특정 테이블 스키마 조회

  * .schema classmates

    ```sql
    .schema classmates
    
    
    CREATE TABLE classmates(
      id INTEGER PRIMARY KEY,
      name TEXT
    );
    ```

* 값 추가

  * INSERT INTO [테이블이름] VALUES [column 값];

    ```sql
    INSERT INTO classmates VALUES (1, '김철수');
    INSERT INTO classmates VALUES (2, '김영희');
    ```

* 테이블 조회

  * SELECT * FROM [테이블 이름];

    ```sql
    SELECT * FROM classmates;  //전부출력
    
    1 | 김철수
    2 | 김영희
    .headers on                 //출력시 column 이름 추가
    .mode column
    SELECT * FROM classmates;
    
    id  name
    --  ----
    1   김철수
    2   김영희
    SELECT name FROM classmates; // 이름만 추가
    
    name
    ----
    김철수
    김영희
    ```

  * \* 는 column 전부 다 보여주는 것, \* 자리에 특정 column(ex. name)만 넣어서 보여 줄 수도 있음

* Primary Key 설정하지 않았을 때

  * SELECT (rowid), * FROM [테이블이름];

  * rowid는 SQL에서 자동으로 제공하는 PK. 값이 1씩 증가함

    ```sql
    SELECT rowid, * FROM classmates;
    
    rowid  name  age  address
    -----  ----  ---  -------
    1      홍길동   23   
    2      홍길동   23     서울
    3      김철수   40     서울
    ```

* 테이블 삭제

  * DROP TABLE [테이블이름];

    ```sql
    DROP TABLE classmates;
    ```

* 필드 제약 조건

  - NOT NULL : NULL 값 입력 금지

  - UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)

  - PRIMARY KEY : 테이블에서 반드시 하나 NOT NULL + UNIQUE

  - FOREIGN KEY : 외래키. 다른 테이블의 Key

  - CHECK : 조건으로 설정된 값만 입력 허용

  - DEFAULT : 기본 설정 값

    ```sql
    CREATE TABLE students(
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      age INTEGER DEFAULT 1 CHECK (0 < age)
    );
    ```

    > * id 는 integer 이고 유일키
    > * name 은 text 이고 빈칸 불가
    > * age는 integer 이고 기본값이 1이며 양수
    >   * 음수값 입력시 `Runtime error : CHECK constraint failed : 0 < age`

<h5>CREATE</h5>

##### INSERT

- 테이블에 단일 행 삽입
  - INSERT INTO 테이블 이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
  
- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력
  - INSERT INTO 테이블 이름 VALUES (값1, 값2, 값3);
  
  ```sql
  CREATE TABLE classmates(
    name TEXT,
    age INT,
    address TEXT
  )
  
  INSERT INTO classmates VALUES ('홍길동', 23);
  Parse error: table classmates has 3 columns but 2 values were supplied
  -- 3개의 컬럼이 존재하는데 두 개 컬럼의 값만 입력 되었으므로 error가 뜸
  
  INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
  .headers on
  .mode column
  SELECT * FROM classmates;
  
  name  age  address
  ----  ---  -------
  홍길동  23
  -- 3개의 컬럼에 값을 모두 집어넣고 싶다면
  INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
  INSERT INTO classmates VALUES ('김철수', 40, '서울')
  -- 2개의 방식 모두 가능
  
  SELECT * FROM classmates;
  
  name  age  address
  ----  ---  -------
  홍길동  23
  홍길동  23     서울
  김철수  40     서울
  -- 여러개의 value를 동시 입력
  INSERT INTO classmates VALUES
  ('홍길동', 30, '서울'),
  ('김철수', 30, '제주'),
  ('이호영', 26, '인천');
  
  SELECT * FROM classmates;
  
  name  age  address
  ----  ---  -------
  홍길동  30     서울
  김철수  30     제주
  이호영  26     인천
  ```



#### READ

##### SELECT

- 테이블에서 데이터를 조회
- SELECT문은 SQLite에서 가장 기본이 되는 문이며, 다양한 절(clause)과 함께 사용
  - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY etc...

```
name  age  address
----  ---  -------
홍길동  30     서울
김철수  30     제주
이호영  26     인천
박민희  29     대구
최혜영  28     전주
```



- **id, name 컬럼 값만 조회**

```
SELECT rowid, name FROM classmates;
rowid  name
-----  ----
1      홍길동  
2      김철수
3      이호영
4      박민희
5      최혜영
```



- **id, name 컬럼 값을 하나만 조회** - `LIMIT` 사용

```
SELECT rowid, name FROM classmates LIMIT 2;
rowid  name
-----  ----
1      홍길동
2      김철수
```



- **id, name 컬럼 값을 세 번째에 있는 값 한 개만 조회** - `LIMIT, OFFSET` 사용

- ```
  OFFSET
  ```

   

  \- 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

  - 예시
    - 문자열 'abcdef' 에서 문자 'c'는 시작점 'a'에서 2의 OFFSET을 지님
    - `SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5`
    - 6번째 행 부터 10개 행을 조회 (6번째 행부터 10개를 출력)

```
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
rowid  name
-----  ----
3      이호영
```



- **id, name 컬럼 값 중에 주소가 서울인 경우를 조회** - `WHERE` 사용

```
SELECT * FROM classmates WHERE address='서울';
name  age  address
----  ---  -------
홍길동  30     서울
```



- **age값 전체를 중복없이 조회** - `DISTINCT` 사용

```
SELECT DISTINCT age FROM classmates;
age
---
30
26
29
28
```



#### UPDATE

- `UPDATE` + 테이블 이름 + `SET` 컬럼1 = 값1, 컬럼2 = 값2 `WHERE` 조건;

```sql
UPDATE classmates SET address='서울' WHERE rowid=5;

-- 전주에서 서울로 변경
rowid  name  age  address
-----  ----  ---  -------
1      홍길동  30     
2      김철수  30    제주
3      이호영  26    인천
4      박민희  29    대구
5      최혜영  28    서울
```

<h4>
	DELETE    
</h4>

- `DELETE FROM` + 테이블이름 + `WHERE` 조건;

```sql
DELETE FROM classmates WHERE rowid = 5;

rowid  name  age  address
-----  ----  ---  -------
1      홍길동  30    서울 
2      김철수  30    제주
3      이호영  26    인천
4      박민희  29    대구
```

### WHERE

- WHERE절에서 사용할 수 있는 연산자

##### 비교 연산자

- `=` , `>`, `>=`, `<`, `<=` 는 숫자 or 문자 값의 대/소, 동일 여부를 확인하는 연산자

##### 논리 연산자

- ```
  AND
  ```

  - 앞에 있는 조건과 뒤에 오는 조건이 모두 참인 경우

- ```
  OR
  ```

  - 앞의 조건이나 뒤의 조건이 참인 경우

- ```
  NOT
  ```

  - 뒤에 오는 조건의 결과를 반대로



#### ⚠️ AND, OR의 우선 순위 주의

[![주의](https://github.com/wdahlia/TIL/raw/master/Database/%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%87%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%B3_2.assets/%E1%84%8C%E1%85%AE%E1%84%8B%E1%85%B4.png)](https://github.com/wdahlia/TIL/blob/master/Database/데이터베이스_2.assets/주의.png)

- ```
  1번째 코드
  ```

   

  : 이 경우, AND가 우선이기 때문에 키가 183이면서 몸무게가 80인 사람 또는 키가 175인 사람을 찾음

  - 즉, 키가 175면서 몸무게가 75인 사람도 해당 됨

- ```
  2번째 코드
  ```

   

  : 이 경우, 괄호 안 값 and 바깥 값이 된다 즉, 키가 175이거나 183인 사람 중 몸무게가 80인 사람

  - 이 경우에는 키가 175면서 몸무게 75인 사람은 해당되지 아니함



#### SQL 사용할 수 있는 연산자

##### 💡BETWEEN 값1 AND 값2

- 값1, 값2 사이의 비교 (값1 <= 비교값 <= 값2)

##### 💡IN(값1, 값2, ...)

- 목록 중에 값이 하나라도 일치, 성공

##### 💡LIKE

- 비교 문자열과 형태 일치
- 와일드카드 (`%` : 0개 이상 문자, `_` : 1개 단일 문자)

##### 💡 IS NULL / IS NOT NULL

- NULL 여부를 확인할 때는 항상 `= 대신 IS` 활용

##### 💡 부정 연산자

- 같지 않다 (`!=`, `^=`, `<>`)
- ~와 같지 않다 (NOT 칼럼명 =)
- ~보다 크지 않다 (NOT 칼럼명 >)



#### 연산자 우선순위

| 1순위     | 2순위 | 3순위            | 4순위 | 5순위 |
| --------- | ----- | ---------------- | ----- | ----- |
| 괄호 `()` | NOT   | 비교 연산자, SQL | AND   | OR    |



#### SQLite Aggregate Functions

##### Aggregate funcion (집계 함수)

- 여러 행으로부터 하나의 결과값을 반환하는 함수

- SELECT 구문에서만 사용됨

- ```
  example
  ```

  - 테이블 전체 행 수를 구하는 **COUNT(\*)**
  - age 컬럼 전체 평균 값을 구하는 **AVG(age)**



##### COUNT

- 그룹의 `항목 수`를 가져옴

##### AVG

- 모든 값의 `평균`을 계산

##### MAX

- 그룹에 있는 모든 값의 `최대값`을 가져옴

##### MIN

##### SUM

### LIKE

- wildcards 사용 예시

#### ORDER BY

- 조회 결과 집합을 **정렬**
- SELECT문에 추가하여 사용
- `ASC` - 오름차순(default)
- `DESC` - 내림차순

### 기본 함수와 연산

#### 문자열 함수

- `SUBSTR` : **문자열 자르기**

  - SUBSTR(*string* FROM *start* FOR *length*)

    ![SUBSTR](https://user-images.githubusercontent.com/108653518/185333417-70d78360-7288-49cb-b144-a98273769174.png)

- `TRIM(문자열)`, `LTRIM(문자열)`, `RTRIM(문자열)` : 문자열 **공백 제거**

  ![TRIM](https://user-images.githubusercontent.com/108653518/185333447-38cf1522-9496-494b-a539-8d6410ba3331.png)

- `LENGTH(문자열)` : 문자열 **길이** [![LENGTH](https://user-images.githubusercontent.com/108653518/185333468-d0003b6d-dd84-472c-8e4b-9b26b777a353.png)](https://user-images.githubusercontent.com/108653518/185333468-d0003b6d-dd84-472c-8e4b-9b26b777a353.png)

- `REPLACE(문자열, 패턴, 변경값)` : **패턴에 일치하는 부분을 변경**

  - REPLACE(*string*, *from_string*, *new_string*)

    ![REPLACE](https://user-images.githubusercontent.com/108653518/185333530-56bad0be-0786-4908-9539-03b256879118.png)

- `UPPER(문자열)`, `LOWER(문자열)` : **대소문자 변경** [![UPLOW](https://user-images.githubusercontent.com/108653518/185334361-c40243b5-ce06-4504-9b0d-e84a721a65e0.png)](https://user-images.githubusercontent.com/108653518/185334361-c40243b5-ce06-4504-9b0d-e84a721a65e0.png)

- `||` : 문자열 합치기(concatenation) [![CONCAT](https://user-images.githubusercontent.com/108653518/185334445-16d2e583-7dd2-47c7-8c87-4e7f641f5fc1.png)](https://user-images.githubusercontent.com/108653518/185334445-16d2e583-7dd2-47c7-8c87-4e7f641f5fc1.png)



#### 숫자 함수

- `ABS(숫자)` : **절대값** [![ABS](https://user-images.githubusercontent.com/108653518/185334660-3988faf8-900d-4d66-830b-f18713dbd7eb.png)](https://user-images.githubusercontent.com/108653518/185334660-3988faf8-900d-4d66-830b-f18713dbd7eb.png)
- `SIGN(숫자)` : **부호** (양수 : 1, 음수 : -1, 0 : 0) [![SIGN](https://user-images.githubusercontent.com/108653518/185334670-a0b6b806-2d58-47c5-9f6d-3eed22249606.png)](https://user-images.githubusercontent.com/108653518/185334670-a0b6b806-2d58-47c5-9f6d-3eed22249606.png)
- `MOD(숫자1, 숫자2)` : 숫자1을 숫자2로 나눈 **나머지** [![MODE](https://user-images.githubusercontent.com/108653518/185334709-2a6b3515-2faa-45ac-a82f-d1ebf00929a4.png)](https://user-images.githubusercontent.com/108653518/185334709-2a6b3515-2faa-45ac-a82f-d1ebf00929a4.png)
- `CEIL(숫자), FLOOR(숫자), ROUND(숫자, 자리)`: **올림**, **내림**, **반올림** [![CFR](https://user-images.githubusercontent.com/108653518/185334731-bf3c6b88-de30-47aa-8b91-1c347b8a1fa6.png)](https://user-images.githubusercontent.com/108653518/185334731-bf3c6b88-de30-47aa-8b91-1c347b8a1fa6.png)
- `POWER(숫자1, 숫자2)` : 숫자1에 숫자2 **제곱** [![POWER](https://user-images.githubusercontent.com/108653518/185334749-c5af62d0-d2e8-487e-a483-daa79c888d90.png)](https://user-images.githubusercontent.com/108653518/185334749-c5af62d0-d2e8-487e-a483-daa79c888d90.png)
- `SQRT(숫자)` : **제곱근** [![SQRT](https://user-images.githubusercontent.com/108653518/185334761-92936001-aa2c-45e6-bb3a-a2aa1ef21b27.png)](https://user-images.githubusercontent.com/108653518/185334761-92936001-aa2c-45e6-bb3a-a2aa1ef21b27.png)



### GROUP BY

> SELECT * FROM *테이블이름* GROUP BY *컬럼1, 컬럼2* ;

- SELECT문의 optional절
- 행 집합에서 요약 행 집합을 만듦
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦

[![groupby](https://user-images.githubusercontent.com/108653518/185334010-34dbbec9-356f-4ff1-b006-8068dc535610.png)](https://user-images.githubusercontent.com/108653518/185334010-34dbbec9-356f-4ff1-b006-8068dc535610.png)

- ⚠️ 문장에 `WHERE절이 포함` 되었다면 반드시 **WHERE절 뒤**에

- `GROUP BY WHERE`

  - example 💡 100번 이상 등장한 성만 출력하고 싶다

  - ```
    SELECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP BY last_name;
    ```

  - ⛔️ **오류 발생!**

    - *Parse error : misuse of aggregate: COUNT()*

  - 조건에 따른 GROUP = **`HAVING절을 사용`**

  - ```
    SELECT last_name, COUNT(last_name) FROM users GROUP BY last_name HAVING COUNT(last_name) > 100;
    ```

  - ##### HAVING

    - 집계함수는 WHERE절의 조건식에서는 사용 불가 (실행 순서에 의해)
    - WHERE로 처리하는 것이 GROUP BY 그룹화보다 순서상 앞서 있기 때문
    - 집계 결과에서 조건에 맞는 값을 따로 활용하기 위해 HAVING 활용



- **집계 함수와 활용하였을 때 의미가 있음**

- GROUP BY에서 활용하는 컬럼을 제외하고는 집계함수를 써야함

  - GROUP BY 활용하는 컬럼을 제외한 컬럼들을 출력시켜도 그 출력의 값은 의미없는 값이 나옴

  - ```
    SELECT last_name, age, COUNT(*) FROM users GROUP BY last_name;
    ```

    - 각 last_name 별로 데이터베이스 전체에서 last_name의 수를 출력, 이때의 **age 출력 값은 의미없는 값**
    - 만약, 이때의 age를 last_name 별로 평균 나이를 알고 싶다면

  - ```
    SELECT last_name, AVG(age), COUNT(*) FROM users GROUP BY last_name;
    ```



- GROUP BY는

   

  결과가 정렬되지 아니함

   

  기존 순서와 바뀜

  - 원칙적으로 내가 **정렬해서 보고 싶다면** ORDER BY



##### SELECT 문장 실행 순서

> **FROM ➡️ WHERE ➡️ GROUP BY ➡️ HAVING ➡️ SELECT ➡️ ORDER BY ➡️ LIMIT/OFFSET**

- ```
  FROM
  ```

   

  \+ 테이블명

  - 테이블을 대상으로

- ```
  WHERE
  ```

   

  \+ 조건식

  - 제약조건에 맞춰 뽑아서

- ```
  GROUP BY
  ```

   

  \+ 칼럼 or 표현식

  - 그룹화한다

- ```
  HAVING
  ```

   

  \+ 그룹조건식

  - 그룹 중에 조건과 맞는 것만을

- ```
  SELECT
  ```

   

  \+ 칼럼명

  - 조회하여

- ```
  ORDER BY
  ```

   

  \+ 칼럼 or 표현식

  - 정렬하고

- ```
  LIMIT/OFFSET
  ```

   

  \+ 숫자

  - 특정 위치의 값을 가져온다



### ALTER TABLE

- `테이블 이름 변경` [![ALTER RENAME1](https://user-images.githubusercontent.com/108653518/185335074-98373f90-6e22-4b2f-970e-291cb8abce73.png)](https://user-images.githubusercontent.com/108653518/185335074-98373f90-6e22-4b2f-970e-291cb8abce73.png)
- `새로운 column 추가` [![ALTER ADD](https://user-images.githubusercontent.com/108653518/185335089-1327540c-2c64-4d3e-92f8-96fb2dfbb37d.png)](https://user-images.githubusercontent.com/108653518/185335089-1327540c-2c64-4d3e-92f8-96fb2dfbb37d.png)
- `column 이름 수정` [![ALTER RENAME2](https://user-images.githubusercontent.com/108653518/185335097-bc867004-e070-461d-a4c2-34a7ebc9770c.png)](https://user-images.githubusercontent.com/108653518/185335097-bc867004-e070-461d-a4c2-34a7ebc9770c.png)
- `column 삭제` [![ALTER DROP](https://user-images.githubusercontent.com/108653518/185335102-b43c074f-947b-42b8-b13e-3360e1050344.png)](https://user-images.githubusercontent.com/108653518/185335102-b43c074f-947b-42b8-b13e-3360e1050344.png)

### CASE

- CASE문은 특정 상황에서 데이터를 변환하여 활용할 수 있음

- ELSE를 생략하는 경우 NULL 값이 저장됨

- column의 이름 CASE가 아니고 다르게 바꾸고 싶다면 `END` 뒤에 `(AS) + column`명

- ```
  CASE WHEN 조건식 THEN 식 WHEN 조건식 THEN 식 ELSE 식 END
  ```

- `example` : healthcare에서 id와 gender가 1, 2일때 각각 남자,여자를 출력

- ```
  SELECT 
      id, 
      CASE 
           WHEN gender = 1 THEN '남자' 
           WHEN gender = 2 THEN '여자' 
      END
  FROM healthcare
  LIMIT 5;
  ```



### 서브쿼리

- **특정한 값을 메인 쿼리에 반환**하여 활용

  - 예를 들어 , WHERE 컬럼 1 = 15 에서 `15라는 값`을 (SELECT 컬럼1 FROM 테이블)

- 실제 테이블에 없는 기준을 이용한 검색 가능

- 소괄호로 감싸서 사용, 메인 쿼리의 칼럼을 모두 사용 가능

- 메인쿼리는 서브 쿼리의 컬럼을 이용할 수 없음

- ```
  SELECT * FROM 테이블 WHERE 컬럼1 = (SELECT 컬럼1 FROM 테이블);
  ```

#### 💡 단일행 서브쿼리

- 서브쿼리의 결과가 0또는 1개인 경우
- **단일행 비교 연산자**와 함께 사용 (`=`, `<`, `<=`, `>=`, `>`, `<>`)

##### 🔻 단일행 서브쿼리 - WHERE에서 활용

- `example 1 `: **users에서 가장 나이가 작은 사람의 수는?**

  [![단일행_서브쿼리](https://user-images.githubusercontent.com/108653518/185550884-f2b72e87-92c6-4a33-b687-a3b995499177.png)](https://user-images.githubusercontent.com/108653518/185550884-f2b72e87-92c6-4a33-b687-a3b995499177.png)

  - 즉, 서브쿼리를 사용하게 되면 **MIN(age)가 변경**이 되더라도 값을 새로 찾을 필요없이 **자동으로 갱신**된다



- `example 2` : **users에서 평균 계좌 잔고보다 높은 사람의 수는?**

  - ```
    SELECT COUNT(*) FROM users WHERE balance > (SELECT AVG(balance) FROM users);
                                               --------------------------------
    >>>                                                    15146.89
    COUNT(*)
    --------
    222
    ```



- `example 3` : **users에서 유은정과 같은 지역에 사는 사람의 수는?**

  [![단일행_서브쿼리1](https://user-images.githubusercontent.com/108653518/185550892-72087a0e-44eb-4ee3-a07d-2754d050ed1d.png)](https://user-images.githubusercontent.com/108653518/185550892-72087a0e-44eb-4ee3-a07d-2754d050ed1d.png)



##### 🔻 단일행 서브쿼리 - SELECT에서 활용

- `example` : **전체 인원과 평균 연봉, 평균 나이를 출력**

  - **서브쿼리 활용 X**

    - ```
      SELECT COUNT(*), AVG(balance), AVG(age) FROM users;
      
      COUNT(*)  AVG(balance)  AVG(age)
      --------  ------------  --------
      1000      151456.89     27.346
      ```

  - **서브쿼리 활용 O**

    - ```
      SELECT
          (SELECT COUNT(*) FROM users) AS 총인원,
          (SELECT AVG(balance) FROM users) AS 평균연봉,
          (SELECT AVG(age) FROM users) AS 평균나이
      FROM users;
      
      총인원      평균연봉      평균나이
      -----  ------------  --------
      1000     151456.89    27.346
      ```



##### 🔻 단일행 서브쿼리 - UPDATE에서 활용

- `example` : **balance를 평균 연봉으로 모두 바꾸기**

  - ```
    UPDATE users SET balance = (SELECT AVG(balance) FROM users);
    ```



#### 💡 다중행 서브쿼리

- 서브쿼리 결과가 2개 이상인 경우
- 다중행 비교 연산자와 함께 사용(`IN`, `EXISTS` 등)

##### 🔻 단일행 서브쿼리 WHERE에서 활용

- `example 1` : **users에서 이은정과 같은 지역에 사는 사람의 수는?**

  [![다중행 _서브쿼리](https://user-images.githubusercontent.com/108653518/185550901-de5407fb-6a54-436c-a9f1-48f9de2d16a8.png)](https://user-images.githubusercontent.com/108653518/185550901-de5407fb-6a54-436c-a9f1-48f9de2d16a8.png)



#### 💡 다중칼럼 서브쿼리

- `example` : **특정 성씨에서 가장 어린 사람들의 이름과 나이**

  [![다중컬럼_서브쿼리](https://user-images.githubusercontent.com/108653518/185550909-d0ee91c5-4ac9-43a7-9e1f-6daf389e8a77.png)](https://user-images.githubusercontent.com/108653518/185550909-d0ee91c5-4ac9-43a7-9e1f-6daf389e8a77.png)

  ### Join

  - 관계형 데이터베이스의 가장 큰 장점, 핵심적인 기능
  - 일반적으로 데이터베이스에는 하나의 테이블에 데이터를 저장하는 것이 아닌 분산하여 저장, 여러 테이블을 결합(Join), 출력, 사용
  - 여러개의 테이블 join하고 싶다면 join은 쿼리 안에서 `테이블 수 - 1`만큼 사용해주어야 한다.
  - 일반적으로 레코드는 기본키(PK)나 외래키(FK) 값의 관계에 의해 결합

  

  #### INNER JOIN

  > 조건에 일치하는(**동일한 값이 있는**) **행**만 반환

  - ```
    SELECT * FROM 테이블1 [INNER] JOIN 테이블2 ON 테이블1.칼럼 = 테이블2.칼럼;
    ```

  

  - `example 1` : **사용자(users)와 각각의 역할을 출력**

    [![innerjoin1](https://user-images.githubusercontent.com/108653518/185887979-cfacaa85-9744-42dc-b67b-0a146bb2c9b6.jpg)](https://user-images.githubusercontent.com/108653518/185887979-cfacaa85-9744-42dc-b67b-0a146bb2c9b6.jpg)

  

  - `example 2` : **staff(2) 사용자(users)를 역할과 함께 출력** (WHERE문 사용)

    [![innerjoin2](https://user-images.githubusercontent.com/108653518/185887987-ee82325a-a4c3-425e-9c81-b704e8543604.jpg)](https://user-images.githubusercontent.com/108653518/185887987-ee82325a-a4c3-425e-9c81-b704e8543604.jpg)

  

  - `example 3` : **사용자(users)와 각각의 역할을 이름의 내림차순으로 출력** (ORDER BY 사용)

    [![innerjoin3](https://user-images.githubusercontent.com/108653518/185887993-d9d06e9b-40b3-4a22-8be1-e9a5691868c7.jpg)](https://user-images.githubusercontent.com/108653518/185887993-d9d06e9b-40b3-4a22-8be1-e9a5691868c7.jpg)

  

  #### OUTER JOIN

  > **동일한 값이 없는 데이터도 반환**할 때 사용

  - 기준이 되는 테이블에 따라 LEFT/RIGHT/FULL을 지정

  - ```
    SELECT * FROM 테이블1 [LEFT|RIGHT|FULL] OUTER JOIN 테이블2 ON 테이블1.칼럼 = 테이블2.칼럼;
    ```

  

  ##### LEFT OUTER JOIN

  - `example 1` : **모든 게시글을 사용자 정보와 함께 출력** (NULL값도 출력)

    [![outerjoin1](https://user-images.githubusercontent.com/108653518/185888004-05eb5bfa-0500-43ea-a600-5bb16f055adf.jpg)](https://user-images.githubusercontent.com/108653518/185888004-05eb5bfa-0500-43ea-a600-5bb16f055adf.jpg)

  

  - `example 2` : **작성자가 있는 모든 게시글을 사용자 정보와 함께 출력** (NULL값 제외, WHERE문 사용)

    [![outerjoin2](https://user-images.githubusercontent.com/108653518/185888014-fc615b24-c631-4fb2-8a62-f40a740046fc.jpg)](https://user-images.githubusercontent.com/108653518/185888014-fc615b24-c631-4fb2-8a62-f40a740046fc.jpg)

  

  ##### FULL OUTER JOIN

  - `example 1` : **모든 게시글과 모든 사용자 정보를 출력**

    [![fullouterjoin](https://user-images.githubusercontent.com/108653518/185888028-45087048-2558-4319-a206-6454921ec500.jpg)](https://user-images.githubusercontent.com/108653518/185888028-45087048-2558-4319-a206-6454921ec500.jpg)

  #### CROSS JOIN

  > **모든 가능한 경우의 수**

  - ```
    SELECT * FROM 테이블1 CROSS JOIN 테이블2;
    ```

  - `example 1` : **users와 role의 CROSS JOIN 결과 출력**

    [![crossjoin](https://user-images.githubusercontent.com/108653518/185888433-befaa6c8-3c55-46d3-b8c6-6ab425db3c6d.jpg)](https://user-images.githubusercontent.com/108653518/185888433-befaa6c8-3c55-46d3-b8c6-6ab425db3c6d.jpg)

  

  #### 3개의 테이블 JOIN

  [![join3tables](https://user-images.githubusercontent.com/108653518/185888454-ca560c2b-5e47-4967-8609-d2531eb627aa.jpg)](https://user-images.githubusercontent.com/108653518/185888454-ca560c2b-5e47-4967-8609-d2531eb627aa.jpg)

**DB 목차**

```
database
참고 사이트
```

- [데이터 모델링(1)](https://mangkyu.tistory.com/27)
- [데이터 모델링(2)](https://inpa.tistory.com/entry/DB-📚-데이터-모델링-1N-관계-📈-ERD-다이어그램)
- [Crow's Foot](https://ppomelo.tistory.com/51)

### 모델링

> 주변에 있는 사람, 사물, 개념 등 다양한 현상을 발생시키는 것들을 일정한 표기법에 의해 나타내는 것

#### 모델링 절차

##### 1️⃣ 개념적 데이터 모델링

> 내가 만든 커뮤니티에 어떤 사람들이 올지? 어떤 글을 남길지 개념적으로 모델링을 해보는 것

- 현실 세계에 대한 인식을 추상

- 데이터의 요구사항을 찾고 분석하는 과정, 핵심 개체(Entity) 사이의 관계를 정의, ERD를 생성하는 것

  ![개념적데이터모델링](../../../알고리즘 문제 사진/개념적데이터모델링.png)

##### 2️⃣ 논리적 데이터 모델링

- 데이터베이스 설계 프로세스의 과정
- 정보의 논리적인 구조와 규칙을 명확하게 표현하는 기법/과정
- 논리 데이터 모델의 `일관성 확보`, `중복 제거` 로 속들이 가장 적절한 엔터티에 배치되도록 함

##### 3️⃣ 물리적 데이터 모델링

- 논리적 데이터 모델이 데이터 저장소로서 어떻게 실제로 저장될 것인가

#### ERD

> Entity Relation Diagram : 개체 관계 모델

정보, 그룹, 관계

- 개념적

카디널리티(Cardinality) : 수적 관계

- 1 : 1 관계 -
- N : M 보통 중개테이블을 만들어줘서 1:N 관계로 바꾼다
- ex) 과제와 유저의 관계는 N:M인데 중개테이블인 과제 제출을 만들어줘서 사용자와 과제 제출 1:N, 과제와 과제제출 1:N

정규화

- 최대한 테이블을 쪼개서 중복을 최소화려는 가장 효율적인 관계를 만들어내는 것에 그 목적이 있음
- 조작 비용을 줄이기 위함 (역정규화의 경우는 값이 변화할 때마다 해당 값들을 모두 수정해주어야함)

역정규화 - 탐색 비용을 줄이기 위함 (정규화에 비해 정보 조회의 속도가 빠름)
