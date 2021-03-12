from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    dist = [[987654321] * (M) for _ in range(N)]
    Q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                Q.append((i, j))
                dist[i][j] = 0
    while Q:
        cur_r, cur_c = Q.popleft()
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M: continue
            if arr[nr][nc] == 'L' and dist[nr][nc] > dist[cur_r][cur_c] + 1:
                dist[nr][nc] = dist[cur_r][cur_c] + 1
                Q.append((nr, nc))
    ans = 0
    for i in dist:
        ans += sum(i)
    print("#{} {}".format(tc, ans))