dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, c, s):
    global maxi

    visited[x][y] = True

    flag = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<N) and (0<=ny<N) and not visited[nx][ny]:
            if arr[nx][ny] < arr[x][y]:
                flag = True
                s += 1
                dfs(nx, ny, c, s)
                s -= 1
            else:
                if arr[nx][ny] - arr[x][y] >= c:
                    continue
                else:
                    flag = True
                    temp = arr[nx][ny]
                    arr[nx][ny] = arr[x][y] - 1
                    s += 1
                    dfs(nx, ny, 0, s)
                    s -= 1
                    arr[nx][ny] = temp

    if not flag:
        visited[x][y] = False
        if maxi < s:
            maxi = s
            return
    else:
        visited[x][y] = False


T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for _ in range(N)]

    largest = 0
    for i in range(len(arr)):
        if largest < max(arr[i]):
            largest = max(arr[i])

    visited = [[False] * N for _ in range(N)]

    maxi = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == largest:
                dfs(i, j, K, 1)
                # print(visited)

    print(f'#{tc} {maxi}')

