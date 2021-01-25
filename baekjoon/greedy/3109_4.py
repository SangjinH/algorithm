import sys

input = sys.stdin.readline

r, c = map(int, input().split())

arr = []
for _ in range(r):
    temp = []
    for j in str(input().rstrip()):
        temp.append(j)
    arr.append(temp)

dx = [-1, 0, 1]
dy = [1, 1, 1]


def find_road(start_x, start_y):
    for i in range(3):
        nx = start_x + dx[i]
        ny = start_y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
            return nx, ny
            break
    return -1, -1

for i in range(r):
    arr[i][0] = 'x'
    start_x = i
    start_y = 0
    while True:
        nx, ny = find_road(start_x, start_y)
        if (nx, ny) == (-1, -1):
            break

        arr[nx][ny] = 'x'

        if ny == c:
            break

        start_x = nx
        start_y = ny

cnt = 0
for i in range(r):
    if arr[i][c] == 'x':
        cnt += 1

print(cnt)