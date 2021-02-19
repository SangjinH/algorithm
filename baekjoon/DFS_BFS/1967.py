import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, dist = list(map(int, input().split()))
    graph[a].append((b, dist))
    graph[b].append((a, dist))

idx = 1
for i in range(2):
    distance = [INF] * (N+1)
    dijkstra(idx)
    idx = distance.index(max(distance[1:]))

print(max(distance[1:]))