# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
def repeat(num, string):
    result = ''
    for i in string:
        a=i*num
        result = result + a
    return result

T = int(input())
a = ''
for i in range(0, T):
    n , s = input().split()
    n = int(n)
    k = repeat(n, s)
    a = a + k + "\n"
print(a)