# 당신은 게임으로 펫을 기르고 있습니다. 이 펫은 웃는 표정, 슬픈 표정을 가지고 있으며, 만약 죽는다면 '드러눕습니다.'

# 펫에게는 적정 체중이 있습니다. 펫의 실제 체중이 적정 체중의 1/2배를 초과하면서 적정 체중의 2배 미만이라면 펫은 행복합니다. 펫의 실제 체중이 0 이하일 경우 펫은 사망하게 되며, 그 외의 경우 펫은 슬픕니다.

# 당신은 콘솔을 통해 펫에게 아래의 두 가지 작용을 할 수 있습니다.

# 'E'와 숫자를 입력해 펫을 운동시킬 수 있습니다. 입력된 숫자(n)만큼의 시간(분; minute)이 지나면 펫의 실제 체중이 n 감소합니다.
# 'F'와 숫자를 입력해 펫에게 먹이를 줄 수 있습니다. 입력된 숫자(n)만큼 펫에게 먹이를 주면 펫의 실제 체중이 n 증가합니다.
# 각 작용에 입력할 수 있는 숫자는 1 이상, 999 이하의 정수입니다. 매 작용이 끝날 때마다 펫은 자신의 상태를 표시하며, 펫이 중간에 죽는다면 이후의 작용은 무시됩니다.

# Faliure
import sys

input = sys.stdin.readline


def chk(fit_weight, current_weight):
    while True:
        act, num = input().split()
        if act == "#":
            status = stat(fit_weight, current_weight)
            return status
        else:
            if act == "E":
                current_weight -= int(num)
            elif act == "F":
                current_weight += int(num)
            if current_weight <= 0:
                current_weight = -10000000


def stat(fit_weight, current_weight):
    if fit_weight < 0:
        status = "RIP"
    elif int((fit_weight / 2)) < current_weight < (fit_weight * 2):
        status = ":-)"
    else:
        status = ":-("
    return status


while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    print(chk(num1, num2))

# 긁풀
if __name__ == "__main__":
    cnt = 0
    while True:
        o, w = map(int, input().split())
        if o == 0 and w == 0:  # "0 0" 입력 시 모든 시나리오 끝남
            quit()

        die = False
        while True:
            action, n = input().split()
            if action == "#" and n == "0":
                break

            if not die:
                n = int(n)
                if action == "E":
                    w -= int(n)
                elif action == "F":
                    w += int(n)

            if w <= 0:  # 사망
                die = True

        cnt += 1
        if w <= 0:
            print("%d RIP" % cnt)
        elif o / 2 < w < o * 2:
            print("%d :-)" % cnt)
        else:
            print("%d :-(" % cnt)
