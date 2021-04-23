import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)
#
#
# def union(parent, v1, v2):
#     root_v1 = find_parent(parent, v1)
#     root_v2 = find_parent(parent, v2)
#     if root_v1 < root_v2:
#         parent[v2] = root_v1
#         for node in range(1, len(parent)):
#             if parent[node] == root_v2:
#                 parent[node] = root_v1
#     else:
#         parent[v1] = root_v2
#         for node in range(1, len(parent)):
#             if parent[node] == root_v1:
#                 parent[node] = root_v2