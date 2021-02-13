import sys

input = sys.stdin.readline
import heapq
INF = 10001
import copy


def dijkstra(start, new_dist):
    q = []
    heapq.heappush(q, (0, start))

    while q:

        dist, now = heapq.heappop(q)
        if new_dist[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < new_dist[i[0]]:
                new_dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

            if new_dist[start] < 0:
                return True
    return False


tc = int(input())
for _ in range(tc):
    n, m, w = list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n+1)
    for _ in range(m):
        s, e, t = list(map(int, input().split()))
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = list(map(int, input().split()))
        graph[s].append((e, -t))

    for i in range(1, n + 1):
        new_dist = copy.deepcopy(distance)
        result = 'NO'
        if dijkstra(i, new_dist):
            result = 'YES'
            break
    print(result)
