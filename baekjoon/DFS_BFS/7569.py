# https://www.acmicpc.net/problem/7569
# 백준 7569번, BFS 토마토농장
import sys

input = sys.stdin.readline

dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dx = [0, 0, -1, 1, 0, 0]


def bfs(arr, start_z, start_y, start_x, h, n, m):
    arr[start_z][start_y][start_x] = 1

    for i in range(6):
        nz = start_z + dz[i]
        ny = start_y + dy[i]
        nx = start_x + dx[i]

        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and arr[nz][ny][nx] == 0:
            arr[nz][ny][nx] = 1
    return False


m, n, h = map(int, input().rstrip().split())
arr = []
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().rstrip().split())))
    arr.append(temp)

cnt = 0
anik = int(1e9)
while anik == 0:

    for i in range(h):
        for j in range(n):
            for k in range(m):
                bfs(arr, i , j, k, h, n, m)

    anik = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == -1:
                    anik += 1
    cnt += 1

print(cnt)