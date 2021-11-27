import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start, n):
    distance = [INF] * (n + 1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


T = int(input())
for _ in range(T):

    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    temp = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a, b) == (h, g) or (a, b) == (g, h):
            temp = d
        graph[a].append([b, d])
        graph[b].append([a, d])

    destinations = []
    for _ in range(t):
        destinations.append(int(input()))
    destinations.sort()

    answer = []
    for destination in destinations:
        check = dijkstra(s, n)[destination]
        dist1 = dijkstra(s, n)[h] + temp + dijkstra(g, n)[destination]
        dist2 = dijkstra(s, n)[g] + temp + dijkstra(h, n)[destination]
        if check in [dist1, dist2]:
            answer.append(destination)

    print(" ".join(map(str, answer)))