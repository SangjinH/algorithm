import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
INF = int(1e9)


graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
routes = [0 for _ in range(n+1)]

for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

# print(graph)

def dijkstra(start):
    global distance
    global routes
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, now = heapq.heappop(q)
        #
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                # print(now)
                routes[i[0]] = now
                # print(routes)
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)

# print(distance)
# print(routes)
#

print(n-1)
for i in range(2, n+1):
    print(i, routes[i])