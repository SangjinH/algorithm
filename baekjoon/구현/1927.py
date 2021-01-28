# https://www.acmicpc.net/problem/1927

import heapq
import sys
input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if not q:
            print(0)
        else:
            pop_num = heapq.heappop(q)
            print(pop_num)
    else:
        heapq.heappush(q, num)
