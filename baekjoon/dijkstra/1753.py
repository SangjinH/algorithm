# https://www.acmicpc.net/problem/1753
# 백준 1753번, 다익스트라 최단경로

import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


v, e = map(int, input().rstrip().split())
start = int(input().rstrip())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])