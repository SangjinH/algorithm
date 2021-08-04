import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

INF = int(1e9)


def dijkstra(start, arrive):

    distance = [INF] * (n+1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            # print("cost", cost)

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # print(distance)
    return distance[arrive]


graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, d, c = map(int, input().split())
    graph[s].append((d, c))

start, arrive = map(int, input().split())

print(dijkstra(start, arrive))