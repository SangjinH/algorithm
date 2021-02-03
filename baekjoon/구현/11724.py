# https://www.acmicpc.net/problem/11724
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, dest = map(int, input().split())
    graph[start].append(dest)

for i in graph[1:]:
    q = deque([])
    if len(i) != 0:
