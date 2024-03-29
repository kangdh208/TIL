<h1> Algorithm 기본</h1>

<h2>
    리스트(List)
</h2>

<h4>
    배열(array)
</h4>

> 여러 데이터들이 연속된 메모리 공간에 저장되어 있는 자료구조

* 인덱스(Index)를 통해 데이터에 빠르게 접근
* 배열의 길이는 변경 불가능 → 길이를 변경하고 싶다면 새로 생성
* 데이터 타입은 고정

| 메모리 주소 | 1000 | 1004 | 1008 | 1012 | 1016 | 1020 | 1024 |
| ----------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 데이터      | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| 인덱스      | A[0] | A[1] | A[2] | A[3] | A[4] | A[5] | A[6] |

<h4>
    연결 리스트(Linked List)
</h4>


> 데이터가 담긴 여러 노드들이 순차적으로 연결된 형태의 자료구조

* 맨 처음 노드부터 순차적으로 탐색
* 연결리스트의 길이 자유롭게 변경 가능 → 삽입, 삭제가 편리
* 다양한 데이터 타입 저장
* 데이터가 메모리에 연속적으로 저장되지 않음

<h4>
    배열 VS 연결리스트
</h4>

* 배열은 리스트로 인덱스를 통해 접근
* 연결리스트는 리스트로 가변 길이를 이용해 활용

| 인덱스 | A[0] | A[1] | A[2] | A[3] | A[4] | A[5] |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- |
| 주소   | 2456 | 3882 | 6428 | 1003 | 2938 | 8372 |

| 데이터 | 0    | 1.5  | 2    | 3    | "a"  | [1,2] |
| ------ | ---- | ---- | ---- | ---- | ---- | ----- |

<h3>
    파이썬의 리스트
</h3>

1. 리스트의 메서드
   1. .append( ) : 리스트 맨 끝에 새로운 원소 삽입
   2. .pop( )        : 특정 인덱스에 있는 원소를 삭제 및 반환
   3. .count( )     : 리스트에서 해당 원소의 개수를 반환
   4. .index( )      : 리스트에서 처음으로 원소가 등장하는 인덱스 반환
   5. .sort( )         : 리스트를 오름차순으로 정렬, reverse=True 옵션을 통해 내림차순으로 정렬 가능
   6. .reverse( )   : 리스트의 원소들의 순서를 거꾸로 뒤집기
2. 리스트 관련 내장함수
   1. len( )            : 리스트의 길이(원소의 개수)를 반환
   2. sum( )          : 리스트의 모든 원소의 합을 반환
   3. max( )          : 리스트의 원소 중 최대값을 반환
   4. min( )           : 리스트의 원소 중 최소값을 반환
   5. sorted( )      : 오름차순으로 정렬된 새로운 리스트 반환, 원본 리스트는 변화 없음
   6. reversed( )  : 리스트의 순서를 거꾸로 뒤집은 새로운 객체 반환, 원본 리스트는 변화 없음

<h2>
    문자열(String)
</h2>

1. 문자열의 메서드
   1. .split( )         : 문자열을 일정 기준으로 나누어 리스트로 반환
      * 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 기준으로 설정
   2. .strip( )         : 문자열의 양쪽 끝에 있는 특정 문자를 모두 제거한 새로운 문자열 반환
      * 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 제거 문자로 설정
      * 제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거
   3. .find( )          : 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환,  찾는 문자가 없다면 -1을 반환
   4. .index( )       : 특정 문자가 처음으로 나타나는 위치(인덱스)를 반환, 찾는 문자가 없다면 오류 발생
   5. .count( )       : 문자열에서 특정 문자가 몇 개인지 반환, 문자 뿐만 아니라, 문자열의 개수도 확인 가능
   6. .replace( )    : 문자열에서 기존 문자를 새로운 문자로 수정한 새로운 문자열 반환
      * 특정 문자를 빈 문자열("")로 수정하여 마치 해당 문자를 삭제한 것 같은 효과 가능
   7. .join( )           : iterable의 각각 원소 사이에 특정 문자를 삽입한 새로운 문자열 반환
      * 삽입할 문자.join(iterable)
      * 삽입할 문자 : 공백 출력, 콤마 출력 등 원하는 출력 형태를 위해 사용

<h3>
    아스키 코드
</h3>

> 미국 정보교환 표준 부호(American Standard Code for Information Interchange)
>
> 컴퓨터는 비트만 저장하므로 문자를 저장하려고 고안된 체계

* 알파벳을 표현하는 대표 인코딩 방식
* 각 문자를 표현하는데 1byte(8bits) 사용
  * 1bit : 통신 에러 검출용
  * 7bit : 문자 정보 저장 (총 128개)

1. ord(문자)  : 문자 🡪 아스키코드로 변환하는 내장함수
2. chr(ASCII) : 아스키코드 🡪 문자로 변환하는 내장함수

![image-20220803050837746](C:\Users\Donghyeon Kang\Desktop\TIL\3week\Algorithm_기본.assets\image-20220803050837746.png)

<h2>
    딕셔너리(Dictionary)
</h2>

<h3>
    해시 테이블(Hash Table)
</h3>

> 딕셔너리는 해시 테이블(Hash Table)을 이용하여 Key: Value를 저장

- 순서가 없음
- `Key` 는 `immutable (변경 불가능)`
- `해시 함수` : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
  - `매핑` 이란 `하나의 값을 다른 값으로 대응` 시키는 것
- `해시` : 해시 함수를 통해 얻어진 값
- 해시 함수와 해시 테이블을 이용하기 때문에 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다
  - 산술 계산으로 값이 있는 위치를 바로 알 수 있기 때문

<h3>
    리스트와 딕셔너리 비교
</h3>

| 연산 종류   | 딕셔너리(Dictionary) | 리스트(List)   |
| ----------- | -------------------- | -------------- |
| Get Item    | O(1)                 | O(1)           |
| Insert Item | O(1)                 | O(1) 또는 O(N) |
| Update Item | O(1)                 | O(1)           |
| Delete Item | O(1)                 | O(1) 또는 O(N) |
| Search Item | O(1)                 | O(N)           |

> 딕셔너리를 사용하는 경우

- 리스트를 사용하기 힘든 경우

- 데이터에 대한빠른 접근 탐색이 필요한 경우

  - 현실 세계의 대부분의 데이터를 다룰 경우

<h6>
    딕셔너리의 메서드
</h6>

1. .keys()     : `Key` 목록이 담긴 `dict_keys` 객체 반환
2. .values()  : `Value` 목록이 담긴 `dict_values` 객체 반환
3. .items()    : `Key`, `Value` 목록이 담긴 `dict_values` 객체 반환



