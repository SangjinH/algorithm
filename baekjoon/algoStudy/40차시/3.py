import sys

input = sys.stdin.readline
from collections import deque

"""
최소 바꾼 경로이기에 bfs를 적용
"""

primes = [True] * 10000

for i in range(2, int((10000) ** (1 / 2))):
    if primes[i]:
        for j in range(i + i, len(primes), i):
            primes[j] = False

print(primes)


def change(start, end):
    if start == end:
        return 0

    q = deque([])
    q.append([start, 0])
    visited = [False] * 10000
    visited[start] = True

    while q:
        now, cnt = q.popleft()
        if now == end:
            return cnt
        if now < 1000:
            continue


T = int(input())
for _ in range(T):
    N1, N2 = map(int, input().split())
    change(N1, N2)
