# DFS

n = int(input())
visited = [False] * (n+1)
networks = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    networks[a].append(b)
    networks[b].append(a)

# print(networks)
def dfs(graph, v, visited):
    visited[v] = True
    # print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(networks,1,visited)

print(visited.count(True)-1)