# https://www.acmicpc.net/problem/2589
import sys

input = sys.stdin.readline
import copy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(start, map):
    arr = copy.deepcopy(map)
    q = deque([start])
    # print(q)
    arr[start[0]][start[1]] = 0

    distances = []
    while q:
        # print(q)
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                distances.append(arr[nx][ny])
                q.append((nx, ny))
    # print(arr)
    return max(distances)


n, m = map(int, input().split())

map = []
for _ in range(n):
    temp = []
    for i in input().rstrip():
        if i == 'L':
            temp.append(1)
        else:
            temp.append(0)
    map.append(temp)

# print(map)
lands = []
for i in range(n):
    for j in range(m):
        if map[i][j] == 1:
            lands.append((i, j))

maxes = []
for i in lands:
    maxes.append(bfs(i,map))

print(max(maxes))
