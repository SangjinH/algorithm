from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(input()) for _ in range(N)]
    visited = [[5000]*M for _ in range(N)]

    water_list = deque([])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                water_list.append((i, j))
                visited[i][j] = 0

    while water_list:
        x, y = water_list.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 'L' and visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    water_list.append((nx, ny))
    ans = 0
    for i in visited:
        ans += sum(i)

    print(f'#{tc} {ans}')