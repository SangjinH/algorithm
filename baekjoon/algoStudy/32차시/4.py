import sys
input = sys.stdin.readline
from collections import deque

def find_sides(n, m, arr):
    visited = [[False] * m for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    visited[0][0] = True

    start = [0, 0]
    q = deque()
    q.append([0, 0])
    melt_list = []

    while q:
        x, y = q.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = x + dx
            ny = y + dy

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    check[nx][ny] += 1
                    if check[nx][ny] >= 2:
                        if [nx, ny] not in melt_list:
                            melt_list.append([nx, ny])
                else:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    # print(check)
    return melt_list


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
while find_sides(N, M, arr):
    answer += 1
    melt_list = find_sides(N, M, arr)
    for i in melt_list:
        arr[i[0]][i[1]] -= 1

print(answer)