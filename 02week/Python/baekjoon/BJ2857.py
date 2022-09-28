# 5명의 요원 중 FBI 요원을 찾는 프로그램을 작성하시오.

# FBI요원은 요원의 첩보원명에 FBI가 들어있다. 

FBI = []
for i in range(5):
    codename = input()
    if 'FBI' in codename:
        FBI.append(i+1)
if len(FBI) == 0:
    print("HE GOT AWAY!")
else:
    print(*FBI, sep=' ')