import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(arr, x, y):
    q = deque([(x, y)])
    arr[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n) and arr[nx][ny] == 1:
                cnt += 1
                arr[nx][ny] = 0
                q.append((nx, ny))

    return cnt


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().rstrip())))
apt = 0
counts = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            apt += 1
            counts.append(bfs(arr, i, j))
counts.sort()
print(apt)
for i in range(len(counts)):
    print(counts[i])
