# https://www.acmicpc.net/problem/1260
# 백준 1260번, DFS BFS
import sys

input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

# print(graph)

seq = []
visited = [False] * (n+1)
def dfs(graph, start, visited):
    visited[start] = True
    seq.append(start)

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, v, visited)
for i in seq:
    print(i, end=' ')
print()

seq = []
visited = [False]*(n+1)
def bfs(graph, start, visited):
    q = deque([start])
    seq.append(start)
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                seq.append(i)
                q.append(i)
bfs(graph, v, visited)
for i in seq:
    print(i, end=' ')