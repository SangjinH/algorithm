import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (N+1)
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


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, destination, cost = list(map(int, input().split()))
    graph[start].append((destination, cost))


for i in range(1, N+1):
    for j in dijkstra(i)[1:]:
        if j == INF:
            print(0, end=' ')
        else:
            print(j, end=' ')

    print()