# 상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.

# 각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.

# 상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

T = int(input())
work = {}
for i in range(T):
    name, log = input().split()
    if log == 'enter':
        work[name] = 'enter'
    else:
        del work[name]
work = sorted(work.keys(), reverse=True)
for k in work:
    print(k)
