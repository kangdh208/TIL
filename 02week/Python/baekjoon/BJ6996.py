# 두 단어 A와 B가 주어졌을 때, A에 속하는 알파벳의 순서를 바꾸어서 B를 만들 수 있다면, A와 B를 애너그램이라고 한다.

# 두 단어가 애너그램인지 아닌지 구하는 프로그램을 작성하시오.

N = int(input())
for _ in range(N):
    A, B = input().split()
    a = sorted(list(A))
    b = sorted(list(B))
    if a == b:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')