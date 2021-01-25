# https://www.acmicpc.net/problem/3109
# 빵집

import sys
input = sys.stdin.readline

dx = [-1, 0, 1]
dy = [ 1, 1, 1]



def bfs(start_x, start_y):
    arr[start_x][start_y] = 1

    x = start_x
    y = start_y

    while True:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<r and 0<=ny<c and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                x = nx
                y = ny
                continue

            if nx == start_x and ny == start_y:
                return False
                break
            if ny == c:
                return True
                break

r, c = map(int, input().split())

arr = []
for _ in range(r):
    temp = []
    for i in str(input().rstrip()):
        if i == '.':
            temp.append(0)
        else:
            temp.append(1)
    arr.append(temp)

cnt = 0
for i in range(r):
    if bfs(i, 0):
       cnt += 1

