import sys
from collections import defaultdict
from copy import deepcopy
input = sys.stdin.readline

def dfs(start, new_visited, road, dist):
    global ans
    if len(road) == len(new_visited)-1:
        if dist < ans:
            ans = dist
            return

    new_visited[start] = True
    for i in graph[start]:
        if not new_visited[i[0]]:
            road += [start]
            dist += int(i[1])
            dfs(i[0], new_visited, road, dist)
            road.pop()
            dist -= int(i[1])



N = int(input())
graph = defaultdict(list)

for _ in range(N):
	start, dest, dist = list(input().split())
	graph[start].append((dest, dist))
	graph[dest].append((start, dist))

distance = defaultdict(list)
visited = defaultdict(list)
for i in graph.keys():
	distance[i] = 10000
	visited[i] = False


ans = 100000
for i in graph.keys():
    new_distance = deepcopy(distance)
    new_visited = deepcopy(visited)
    dfs(i, new_visited, [], 0)


if ans == 100000:
    print()
else:
    print(ans)