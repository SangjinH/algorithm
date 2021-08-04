import sys
input = sys.stdin.readline

sys.setrecursionlimit(999)

INF = int(1e9)

n, m = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
visited[0][0] = True

ans = INF


def dfs(x, y, broken, total):
    global ans

    if x == n-1 and y == m-1:
        ans = min(ans, total)
        return

    for dx, dy in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
        nx = x + dx
        ny = y + dy

        # 범위 내에 존재하고
        if 0<=nx<n and 0<=ny<m:

            # 가려고하는 곳이 벽이라면
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                # 아직 벽을 깨지 않았다면
                if not broken:
                    broken = True
                    visited[nx][ny] = True
                    dfs(nx, ny, broken, total+1)
                    broken = False
                    visited[nx][ny] = False
            # 가려고하는 곳이 길이라면
            elif arr[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, broken, total+1)
                visited[nx][ny] = False


dfs(0, 0, False, 1)

if ans == INF:
    print(-1)
else:
    print(ans)