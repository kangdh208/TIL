# 신생국가 CTP공국은 자신들만의 글자가 없다. CTP공국의 왕 준형이는 전 세계 표준 언어인 알파벳을 사용하기로 했다. 하지만 숫자에 미친 사람들이 모인 CTP공국 주민들은 알파벳을 사용할 때 평범한 알파벳이 아니라 쓰려고 하는 알파벳이 앞에서부터 몇 번째 알파벳인지를 의미하는 숫자로 나타낸다. 예를 들어 ‘A’는 ‘1’로, ‘Z’는 ‘26’로 나타낸다.

# CTP공국은 현재 부흥 중이라 새로 국민이 되고자 하는 사람이 많다. 하지만 아무나 CTP공국의 국민이 될 수는 없는 법. CTP공국의 이민국장 인덕이는 이민 신청자들이 CTP 공국의 글자체계를 잘 알고 있는지 확인하는 시험문제를 내기로 했다.

# 시험문제는 두 가지 종류로 구분된다. CTP공국의 글자가 주어졌을 때 알파벳을 쓰는 문제와 알파벳이 주어졌을 때 CTP공국의 글자를 쓰는 문제 두 가지이다.

# 너무 많은 이민 신청자들 때문에 시험문제 채점에 골치가 아픈 인덕이를 위해 주어진 시험문제의 정답을 알려주는 프로그램을 작성하라.

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num, alpha = input().split()
    lst = list(input().split())
    CTP = []
    if alpha == "C":
        for i in lst:
            char = str(ord(i) - 64)
            CTP.append(char)
    else:
        for i in lst:
            CTP.append(chr(int(i) + 64))

    print(" ".join(CTP))
