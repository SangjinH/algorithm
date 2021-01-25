import sys

input = sys.stdin.readline
from collections import deque

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(arr, start_x, start_y):
    arr[start_x][start_y] = 0
    q = deque([(start_x, start_y)])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < num) and (0 <= ny < num) and arr[nx][ny]==-1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


n = int(input().rstrip())  # 테스트 케이스의 갯수

for _ in range(n):
    num = int(input().rstrip())
    arr = [[-1] * num for _ in range(num)]
    start_x, start_y = map(int, input().rstrip().split())
    target_x, target_y = map(int, input().rstrip().split())
    bfs(arr, start_x, start_y)
    print(arr[target_x][target_y])
