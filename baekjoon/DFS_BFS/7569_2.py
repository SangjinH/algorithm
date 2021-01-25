import sys

input = sys.stdin.readline

dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dx = [0, 0, -1, 1, 0, 0]


def bfs(arr, start_z, start_x, start_y):
    arr[start_z][start_x][start_y] = 1

    for i in range(6):
        nz = start_z + dz[i]
        ny = start_y + dy[i]
        nx = start_x + dx[i]

        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and arr[nz][nx][ny] == 0:
            arr[nz][ny][nx] = 1


m, n, h = map(int, input().rstrip().split())
arr = []
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().rstrip().split())))
    arr.append(temp)
print(arr)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                bfs(arr,i,j,k)
print(arr)