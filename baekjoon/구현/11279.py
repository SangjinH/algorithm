# https://www.acmicpc.net/problem/11279
import sys
import heapq
input = sys.stdin.readline

n = int(input())

q = []

for _ in range(n):
    num = int(input())

    if not num:
        if len(q):
            print(-heapq.heappop(q))
        else:
            print(0)

    else:
        heapq.heappush(q, -num)
