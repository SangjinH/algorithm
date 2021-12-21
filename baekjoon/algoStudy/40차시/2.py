import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * len(graph)
distance = [0] * len(graph)
total = 0


def dfs(curr):
    visited[curr] = True
    for i in graph[curr]:
        if not visited[i]:
            distance[i] = distance[curr] + 1
            dfs(i)

dfs(1)

for i in range(len(graph)):
    if len(graph[i]) == 1:
        total += distance[i]


if total % 2:
    print("Yes")
else:
    print("No")