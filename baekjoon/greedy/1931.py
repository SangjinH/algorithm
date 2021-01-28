# https://www.acmicpc.net/problem/1931
import sys
input = sys.stdin.readline

n = int(input())

meet_list = []
for _ in range(n):
    meet_list.append(list(map(int, input().split())))
meet_list.sort()

dp = [0] * (2 ** 31 -1)

meeting = sorted(meet_list, key = lambda x : [x[1], x[0]])

