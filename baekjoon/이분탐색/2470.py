# https://www.acmicpc.net/problem/2470

"""
산성용액의 특성값  1 ~ 10억
알칼리용액 특성값 -10억 ~ -1

두 용액을 혼합하여 0에 가장 가까운 용액을 만들려고한다.

"""


import sys
input = sys.stdin.readline

n = int(input())
liquids = sorted(list(map(int, input().split())))


l = 0
r = n-1

result = liquids[0] + liquids[-1]
re_left = 0
re_right = n-1

while l < r:

    temp = liquids[l] + liquids[r]

    # 원점으로부터의 거리가 더 짧으면 갱신
    if abs(temp) < abs(result):
        re_left = l
        re_right = r
        result = temp

        if temp == 0:
            break

    # 음수라면
    if temp < 0:
        l += 1

    else:
        r -= 1

print(liquids[re_left], liquids[re_right])