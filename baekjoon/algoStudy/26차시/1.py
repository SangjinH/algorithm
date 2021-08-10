import sys
input = sys.stdin.readline

from collections import deque


"""
변의 길이는 모두 10
색종이를 겹치도록 놓았을때, 둘레의 길이를 구해라
"""

arr = [[0] * 102 for _ in range(102)]


start_points = []

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1


visited = [[False]*102 for _ in range(102)]


def bfs(x, y):
    r = 0
    visited[x][y] = True

    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nx = x + dx
            ny = y + dy
            # 범위 내에 있고
            if 0<=nx<102 and 0<=ny<102:
                # 방문하지 않은 곳이고
                if not visited[nx][ny]:
                    # 박스를 만나면
                    if arr[nx][ny]:
                        r += 1
                    else:
                        visited[nx][ny] = True
                        q.append((nx, ny))
    return r


ans = 0
for i in range(102):
    for j in range(102):
        # 방문처리되지 않고, 빈 공간이라면 bfs 시작
        if not visited[i][j] and not arr[i][j]:
            ans += bfs(i, j)

print(ans)