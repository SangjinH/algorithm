from collections import deque


# def bfs(graph, start, visited):
#     visited[start] = True
#     q = deque([start])
#     result = []
#     dist = 0
#     while q:
#         now = q.popleft()
#         print('now: ', now)
#
#         for i in graph[now]:
#             if not visited[i[0]]:
#                 visited[i[0]] = True
#                 dist += i[1]
#                 print('dist: ', dist)
#                 q.append(i[0])
#             else:
#                result.append(dist)
#     print(result)

# def dfs(graph, start, visited, dist):
#
#     if visited[start]:
#         return dist
#
#     visited[start] = True
#
#     for i in graph[start]:
#         if not visited[i[0]]:
#             dist += i[1]
#             return dfs(graph, i[0], visited, dist)
import sys
input = sys.stdin.readline
import heapq

def max_dijkstra(start):
    distance[start] = 0
    visited[start] = True
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] > dist:
            continue

        for i in graph[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                cost = dist + i[1]

                if cost > distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

V = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(V):
    nums = list(map(int, input().split()))
    idx = nums[0]
    nums = nums[1:-1]
    for i in range(0, len(nums), 2):
        target, dist = nums[i], nums[i+1]
        graph[idx].append((target, dist))

maxi = 0
idx = 1
for i in range(2):
    visited = [False] * (V+1)
    distance = [0] * (V+1)
    max_dijkstra(idx)

    idx = distance.index(max(distance))

print(max(distance))