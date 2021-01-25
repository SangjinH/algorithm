# https://www.acmicpc.net/problem/1389
import sys

input = sys.stdin.readline
from collections import deque

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = deque([start])

    while q:
        v = q.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[v] + 1
                q.append(i)

    return distance[1:]


results = []
for i in range(1, n + 1):
    results.append(sum(bfs(i)))

print(results.index(min(results))+1)