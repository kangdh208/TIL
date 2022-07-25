# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

N = int(input())
n = input()
lst = []
for i in range(len(n)):
    j = n[i]
    lst.append(int(j))
cnt = sum(lst)
print(cnt)