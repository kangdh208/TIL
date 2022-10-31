# 전쟁에 참여한 화랑이는 적군의 기지에 침투하여 정보를 훔쳐오는 임무를 받았습니다. 화랑이는 야간 전술 보행을 이용하여 직진하며, 야간 전술 보행은 1m/s의 일정한 속도로 나아갈 수 있습니다. 화랑이의 침입 경로에는 경비병들이 각자 일부 구간들을 감시하고 있습니다. 각각의 경비병들이 감시하는 구간은 서로 겹치지 않으며, 일정 시간 동안 근무 후 일정 시간 동안 휴식을 취하는 과정을 반복합니다. 화랑이가 지나가고 있는 위치를 감시하는 경비병이 근무 중이라면 화랑이는 경비병에게 발각되어 즉시 붙잡히게 됩니다. 하지만 해당 위치를 감시하는 경비병이 휴식을 취하고 있으면 화랑이는 무사히 해당 위치를 지나갈 수 있습니다. 경비병의 근무 정보를 모르는 화랑이는 쉬지 않고 전진을 하며, 화랑이가 출발할 때 모든 경비병들이 동시에 근무를 시작합니다.

def solution(distance, scope, times):
    lst = []
    for i in range(len(scope)):
        start, end = sorted(scope[i])
        work, rest = times[i]
        time = start
        while time <= end:
            N = time % (work+rest)
            if 0 < N <=work:
                lst.append(time)
                break
            time += 1
    if len(lst) > 0:
        return sorted(lst)[0]
    else:
        return distance