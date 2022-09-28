# 1부터 주어진 숫자만큼 모두 더한 값을 출력하시오.

# 단, 주어질 숫자는 10000을 넘지 않는다.

n = int(input())
result = 0
printing = '1'
for i in range(1, n+1):
    result += i
for i in range(2, n+1):
    printing = printing+ (f' + {i}')
print(printing , "=", result)