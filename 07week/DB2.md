# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
    id PRIMARY KEY,        
    sido INTEGER NOT NULL, 
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,  
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,   
    va_left REAL NOT NULL, 
    va_right REAL NOT NULL,

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
select count(*) from healthcare;
```

```sqlite
count(*)
1000000
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
select max(age), min(age) from healthcare where age;
```

```sqlite
max(age)|min(age)
18|9
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
select max(height), min(height), max(weight), min(weight) from healthcare where height and weight;
```

```sqlite
max(height)|min(height)|max(weight)|min(weight)
195|130|135|30
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
select count(*) from healthcare WHERE 160<=height AND height<=170;
```

```
count(*)
516930
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql
select * FROM healthcare WHERE is_drinking=1 ORDER BY waist DESC LIMIT 5;
```

```
15583|11|2|11|155|50||1.2|1.2|103|1|1
20143|11|2|9|170|105||0.5|0.5|156|3|1
45103|41|2|10|155|45||0.8|1.0|106|1|1
52074|41|2|11|165|60||||94|1|1
56063|11|1|9|175|75||1.2|1.2|119|2|1
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare where (va_left>1.5 and va_right>1.5) AND is_drinking = 1;
```

```bash
count(*)
1636
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE blood_pressure<120;
```

```
count(*)
360808
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT avg(blood_pressure) FROM healthcare WHERE blood_pressure>=140;
```

```
avg(blood_pressure)
141.689738648599
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT avg(height), avg(weight) FROM healthcare WHERE gender=1;
```

```
avg(height)|avg(weight)
167.452735422145|69.7131620222875
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC limit 2,1;
```

```
id	height	weight
170951	195	85
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT count(*) FROM healthcare WHERE 30<=((weight*10000)/(height*height));
```

```
count(*)
53121
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT id, ((weight*10000)/(height*height)) FROM healthcare WHERE smoking=3 ORDER BY((weight*10000)/(height*height)) DESC LIMIT 5;
```

```
id	((weight*10000)/(height*height))
231431	50
934714	49
722707	48
947281	47
948801	47
```

### 13. (자유 쿼리) 남성(1)의 키(height), 몸무게(weight) 평균을 출력하시오.

```sql
SELECT avg(height), avg(weight) FROM healthcare WHERE gender=1;
```

```
avg(height)	avg(weight)
167.452735422145	69.7131620222875
```

### 14. *(자유 쿼리) BMI 의 평균값을 출력하시오.*

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
SELECT avg(((weight*10000)/(height*height))) FROM healthcare;
```

```
avg(((weight*10000)/(height*height)))
23.709475
```

### 15. (5-1) 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. - not blank 추가

```sql
SELECT id FROM healthcare WHERE is_drinking=1 AND waist>1 ORDER BY waist DESC LIMIT 5;
```

```
id
15583
20143
45103
52074
56063
```

### 16. *(5-2) 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. - not null 추가*

```sql
SELECT id FROM healthcare WHERE is_drinking=1 AND waist NOT NULL ORDER BY waist DESC LIMIT 5;
```

```bash
id
15583
20143
45103
52074
56063
```

