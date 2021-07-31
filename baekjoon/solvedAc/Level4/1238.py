# https://www.acmicpc.net/problem/1238

# 파티장까지 오고가고
# 가장 많은 거리를 오고가는 사람은 누구 ?

import heapq

INF = int(1e9)


def dijkstra(start, n):
    distance = [INF] * (n + 1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, d, t = map(int, input().split())
    graph[s].append((d, t))

dist = dijkstra(x, n)

for i in range(1, n+1):
    if i != x:
        dist[i] += dijkstra(i, n)[x]

print(max(dist[1:]))