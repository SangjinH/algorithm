import sys
input = sys.stdin.readline

# N 은 자연수 or 0

n = int(input())


def solution(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    prev1 = 0
    prev2 = 1
    for i in range(2, n+1):
        now = prev1 + prev2
        prev1 = prev2
        prev2 = now % 1000000007

    return now % 1000000007

print(solution(n))

