# 백준 2178 미로탐색
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(arr, x, y):

    q = deque([(x,y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]==1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


n, m = map(int, input().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

dfs(arr, 0, 0)
print(arr[n-1][m-1])