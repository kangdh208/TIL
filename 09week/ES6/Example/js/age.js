
// 함수 선언과 구현   
function calc() {
    var currentYear = 2022; //올해 년도를 변수에 저장
    // 입력값 변수에 저장
    var birthYear = prompt("태어난 년도를 입력하세요. ","YYYY");
    // 변수 age 초기화
    var age = 0;
    // 나이 구하는 코드 생성
    age = currentYear - birthYear + 1;
    // 출력코드
    document.querySelector("#result").innerHTML = 
                              "당신의 나이는 " + age + "세 입니다.";
    }
