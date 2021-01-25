# 백준 18352
from collections import deque
import sys

def bfs(graph, start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = distance[v] + 1
                queue.append(i)


n, m, k, x = map(int,sys.stdin.readline().rstrip().split())

distance = [-1 for _ in range(n+1)]
distance[x] = 0
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

bfs(graph, x)

for i in range(len(distance)):
    if k == distance[i]:
        print(i)
if k not in distance:
    print(-1)