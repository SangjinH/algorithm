# https://www.acmicpc.net/problem/11725
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque([1])
    parents = [0] * (n+1)
    visited = [False] * (n+1)
    visited[1] = True

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                parents[i] = v
                q.append(i)

    return parents[2:]

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in bfs():
    print(i)