# 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.

n = int(input())
print('True') if (n%2 == 0 and n%3 == 0) else print('False')