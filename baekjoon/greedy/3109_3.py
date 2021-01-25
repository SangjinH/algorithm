# https://www.acmicpc.net/problem/3109
# 파이프연결
import sys

input = sys.stdin.readline

r, c = map(int, input().split())

arr = []
for _ in range(r):
    temp = []
    for j in str(input().rstrip()):
        if j == '.':
            temp.append(0)
        else:
            temp.append(1)
    arr.append(temp)

dx = [-1, 0, 1]
dy = [1, 1, 1]


def dfs(start_x, start_y):
    arr[start_x][start_y] = 1

    while True:
        if start_y == c:
            break

        for i in range(3):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            print(nx)
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                start_x = nx
                start_y = ny
                break

        if nx == start_x and ny == start_y:
            break


for i in range(r):
    dfs(i, 0)

print(arr)
