import sys
input = sys.stdin.readline
from collections import defaultdict

match_stick = [[], [], [1], [7], [4], [2, 5], [0, 6, 9], [8]]


def find_max(N):
    num = ''
    while N > 3:
        num += '1'
        N -= 2

    if N == 2:
        num += '1'
    elif N == 3:
        num = '7' + num

    return num


def find_min(N):
    num = ''
    # 만약 N 이 7보다 작거나 같다면
    while N != 0:
        print(N)

        if N == 7:
            num = '8' + num
            N -= 7

        elif N == 6:
            num = '6' + num
            N -= 6

        elif N == 5:
            num = '2' + num
            N -= 5

        elif N == 4:
            num = '4' + num
            N -= 4

        elif N == 3:
            num = '7' + num
            N -= 3

        elif N == 2:
            num = '1' + num
            N -= 2

        # N이 7보다 크다면
        else:
            if N - 7 >= 2:
                num = '8' + num
                N -= 7
            elif N - 6 >= 2:
                num = '0' + num
                N -= 6

    return num


T = int(input())
for _ in range(T):
    N = int(input())
    print(find_min(N), find_max(N))

