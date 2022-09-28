# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

# 주어질 숫자는 30을 넘지 않는다.

sqar = int(input())
numlst = ['1']
for i in range(1, sqar+1):
    numlst.append(str(2**i))
print(" ".join(numlst))
