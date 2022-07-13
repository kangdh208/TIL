# 숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 
# cube 함수를 호출하여 12의 세제곱 결과를 출력하시오.
def cube(a):
    result = a**3
    return result

n = int(input())
cube_result = cube(n)
print(cube_result)