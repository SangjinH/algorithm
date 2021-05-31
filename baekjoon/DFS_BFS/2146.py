import sys

input = sys.stdin.readline
from collections import deque


def bfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = cnt

    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] != 0:
                visited[nx][ny] = cnt
                q.append((nx, ny))


def find_way():
    pass



N = int(input())
INF = int(1e9)
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
distance = [[INF]*N for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0 and not visited[i][j]:
            bfs(i, j)

print(visited)