# https://www.acmicpc.net/problem/2644
# 촌수
import sys

input = sys.stdin.readline
from collections import deque

INF = int(1e9)

n = int(input())

person_a, person_b = map(int, input().split())

graph = [[] for _ in range(n + 1)]


def bfs(start, arrive):
    chons = [INF] * (n + 1)
    chons[start] = 0
    q = deque([start])

    while q:
        now = q.popleft()

        for i in graph[now]:
            if chons[i] == INF:
                chons[i] = chons[now] + 1
                q.append(i)

    return chons[arrive]


for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


ans = bfs(person_a, person_b)

if ans == INF:
    print(-1)
else:
    print(ans)