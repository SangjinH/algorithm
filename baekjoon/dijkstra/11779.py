# https://www.acmicpc.net/problem/11779
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

    return distance[dest]



n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, dest = map(int, input().split())
distance = [INF] * (n+1)

print(dijkstra(start))