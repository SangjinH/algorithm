# https://www.acmicpc.net/problem/1504
import sys
input = sys.stdin.readline
import heapq

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

must1, must2 = map(int, input().split())

def dijkstra(start, arrive):
    q = []
    distance = [1e9] * (n+1)
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
    return distance[arrive]

p1 = dijkstra(1, must1) + dijkstra(must1, must2) + dijkstra(must2, n)
p2 = dijkstra(1, must2) + dijkstra(must2, must1) + dijkstra(must1, n)

if p1 >= 1e9 and p2 >= 1e9:
    print(-1)
else:
    print(min(p1, p2))