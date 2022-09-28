# 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져. N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 뭔지는 알지? 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.

# 둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어. 아참! 일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야. 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!

# 시간초과
N, M = map(int, input().split())
pokemon= []
for _ in range(N):
    pokemon.append(input())
question = []
for _ in range(M):
    chk = input()
    try:
        chk = int(chk)
        question.append(chk)
    except:
        question.append(chk)
for i in range(len(question)):
    if type(question[i]) == int:
        print(pokemon[question[i]-1])
    else:
        print(pokemon.index(question[i])+1)

# 새풀이
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
dogam = {}
for i in range(N):
    pokemon = input().rstrip()
    dogam[i+1] = pokemon
    dogam[pokemon]=i+1
for j in range(M):
    ask = input().rstrip()
    if ask.isalpha()==False:
        print(dogam[int(ask)])
    else:
        print(dogam[ask])