# https://www.acmicpc.net/problem/1012
# 백준 1012번 BFS, DFS 유기농 배추
import sys

input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr, start_x, start_y, n, m):
    q = deque([(start_x, start_y)])
    arr[start_x][start_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                q.append((nx, ny))

num_case = int(input().rstrip())
for _ in range(num_case):
    m, n, k = map(int, input().rstrip().split())
    arr = [[0]*m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().rstrip().split())
        arr[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                bfs(arr, i, j, n, m)
    print(cnt)