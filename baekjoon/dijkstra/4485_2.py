import sys

input = sys.stdin.readline
import heapq

INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = arr[0][0]

    q = []
    heapq.heappush(q, [arr[0][0], 0, 0])

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + arr[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, [cost, nx, ny])

    return distance[n-1][n-1]


cnt = 1
while True:
    arr = []
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    print("Problem {}: {}".format(cnt, dijkstra()))

    cnt += 1