# https://www.acmicpc.net/problem/4485
import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(arr):
    dp = [[INF] * n for _ in range(n)]
    dp[0][0] = arr[0][0]
    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    q = []
    heapq.heappush(q, [arr[0][0], 0, 0])

    while q:
        c, x, y = heapq.heappop(q)

        if dp[x][y] < c:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:

                cost = c + graphs[nx][ny]

                if cost < dp[nx][ny]:
                    dp[nx][ny] = cost
                    heapq.heappush(q, [cost, nx, ny])

    return dp

graphs = []
while True:
    arr = []
    n = int(input())
    if n == 0:
        break
    else:
        for _ in range(n):
            arr.append(list(map(int, input().split())))
    graphs.append(arr)

    for i in graphs:
        print(dijkstra(i))


