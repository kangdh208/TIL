# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

n = int(input())
star =[]
for i in range(1, n+1):
    if i %2 ==0:
        star.append(' *'*n)
    else:
        star.append('* '*n)
for j in range(len(star)):
    print(star[j])