# https://www.acmicpc.net/problem/4963
# 백준 4963번, BFS 섬의 갯수

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]


def bfs(graph, start, m, n):
    q = deque([start])
    graph[start[0]][start[1]] = 0
    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


case_list = []
while True:
    m, n = list(map(int, input().rstrip().split()))

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().rstrip().split())))
    if (n, m) == (0, 0):
        break
    else:
        cnt = 0
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    cnt += 1
                    bfs(graph, [i, j], m, n)
        print(cnt)
