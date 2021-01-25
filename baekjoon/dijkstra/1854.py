# https://www.acmicpc.net/problem/14284
import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
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

    return distance[d]

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

s, d = map(int, input().split())

print(dijkstra(s))