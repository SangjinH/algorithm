# 구현 로봇청소기 14503번
import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
r, c, d = map(int, input().rstrip().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().rstrip().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def post_d(d):
    d = (d + 4) % 4
    return d


def find(r, c, d):
    global empty
    cnt = 1
    x = r
    y = c
    array[x][y] = 2
    while True:
        dc = d
        for i in range(4):
            empty = 0
            dc = post_d(d)
            nx = x + dx[dc]
            ny = y + dy[dc]

            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                cnt += 1
                x = nx
                y = ny
                array[x][y] = 2
                d = dc
                empty = 1
                break

        if empty == 0:
            if d == 0:
                x += 1
            elif d == 1:
                y -= 1
            elif d == 2:
                x -= 1
            elif d == 3:
                y += 1

            if array[x][y] == 1:
                break
    return cnt


res = find(r, c, d)
print(res)
