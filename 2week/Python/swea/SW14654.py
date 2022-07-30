# 신용 카드를 만들려면 아래 두 가지의 조건을 모두 만족해야 한다.

# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
# EX) 6471-6836-9525-5276
# EX) 3029192045012901

# 카드 번호가 주어졌을 때 해당 번호로 신용카드를 만들 수 있는지 판별하는 프로그램을 작성하시오.

def dashchk(oldcard): #-없애기
    card = ''
    for i in range(len(oldcard)):
        if oldcard[i] != '-':
            card += oldcard[i]
    return card

def numchk(cardnum): #첫숫자가 3569니?
    if len(cardnum) == 16: #길이는?16이야?
        if cardnum[0] in '34569':
            return 1 #어, 둘다맞아
        else:
            return 0 #아니
    else:
        return 0 #아뉜데

T = int(input())
for z in range(T):
    number = input()
    cardnumber = dashchk(number) # dash없애고
    print(f'#{z+1} {numchk(cardnumber)}') #확인하기