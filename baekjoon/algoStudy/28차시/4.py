import sys
input = sys.stdin.readline

from collections import deque
import copy

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

graph = [[]]


def find_island():
    number = 1

    for i in range(n):
        for j in range(n):
            if map[i][j] == 1 and not visited[i][j]:
                temp = []
                temp.append([i, j])

                q = deque()
                q.append([i, j])
                map[i][j] = number
                visited[i][j] = True

                while q:
                    x, y = q.popleft()

                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        nx = x + dx
                        ny = y + dy

                        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and map[nx][ny] != 0:
                            visited[nx][ny] = True
                            map[nx][ny] = number
                            q.append([nx, ny])
                            temp.append([nx, ny])
                number += 1
                graph.append(temp)

ans = int(1e9)

def find_min_dist():
    global ans

    for i in range(1, len(graph)):
        q = deque(graph[i])
        N_visited = copy.deepcopy(visited)
        flag = False

        while q:
            x, y = q.popleft()

            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx = x + dx
                ny = y + dy

                # 범위 내에 있고
                if 0 <= nx < n and 0 <= ny < n:

                    if map[nx][ny] > 0 and map[nx][ny] != i:
                        ans = min(ans, N_visited[x][y])
                        flag = True
                        break

                    elif map[nx][ny] == i:
                        continue

                    elif map[nx][ny] == 0 and not N_visited[nx][ny]:
                        N_visited[nx][ny] = N_visited[x][y] + 1
                        q.append([nx, ny])

            if flag:
                break


find_island()
find_min_dist()
if ans == 0:
    print(ans)
else:
    print(ans-1)