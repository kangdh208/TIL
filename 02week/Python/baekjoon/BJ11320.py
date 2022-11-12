# 무엇이든 덮어버리는 것을 좋아하는 구사과는 한 변의 길이가 A인 정삼각형을 한 변의 길이가 B인 정삼각형으로 완전히 덮어버리고자 한다.

# 두 개의 정수 A, B가 주어지고, B ≤ A 이고, A를 B로 나눌 수 있을 때, 한 변의 길이가 A인 정삼각형을 완전하게 덮기 위한, 한 변의 길이가 B인 정삼각형의 개수를 구하라.
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A**2 // B**2)
