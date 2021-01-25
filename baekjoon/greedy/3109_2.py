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
# print(arr)

dx = [-1, 0, 1]
dy = [1, 1, 1]


def find_road(start_x, start_y):
    for i in range(3):
        nx = start_x + dx[i]
        ny = start_y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == 0:
            return nx, ny
            break
    return -1, -1

for i in range(r):
    start_x = i
    start_y = 0
    arr[start_x][start_y] = 1

    while True:
        nx, ny = find_road(start_x, start_y)
        if (nx, ny) == (-1, -1):
            break

        else:
            arr[nx][ny] = 1
            start_x = nx
            start_y = ny
        if start_y == c:
            break

cnt = 0
for i in range(r):
    if arr[i][-1] == 1:
        cnt += 1
print(cnt)