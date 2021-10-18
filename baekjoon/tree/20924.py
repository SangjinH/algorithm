import pprint
import sys
input = sys.stdin.readline
from collections import defaultdict

# 루트노트, 기가노드, 가지노드

N, R = map(int, input().split())

routes = [[0] * (N+1) for _ in range(N+1)]
trees = defaultdict(list)
visited = [False] * (N+1)

for _ in range(N-1):
    a, b, d = map(int, input().split())
    routes[a][b] = d
    routes[b][a] = d

    trees[a].append(b)

giga = 0
dist_giga = 0
for k in trees.keys():
    if len(trees[k]) > 1:
        giga = k
        break
    else:
        dist_giga += routes[k][trees[k][0]]

maxi = 0

def dfs(node, total):
    global maxi
    # 끝단 노드라면
    if not trees[node]:
        if total > maxi:
            maxi = total
        return

    for i in trees[node]:
        dfs(i, total+routes[node][i])


def find_max_dist(giga):
    for i in trees[giga]:
        dfs(i, routes[giga][i])

find_max_dist(giga)

print(dist_giga, maxi)