# 단지번호 붙이기
import sys
from collections import deque
import copy

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

total_list = []


def bfs(arr, x, y):
    q = deque([(x, y)])

    cnt = 1

    arr[x][y] = 0

    while q:
        # print(q)
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                cnt += 1
                arr[nx][ny] = 0
                q.append((nx, ny))

    total_list.append(cnt)


n = int(input().rstrip())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

check = copy.deepcopy(arr)

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            bfs(arr, i, j)


total_list.sort()
print(len(total_list))
for i in total_list:
    print(i)
