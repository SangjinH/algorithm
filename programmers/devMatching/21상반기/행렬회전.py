from collections import deque


def rotate(sx, sy, fx, fy, arr):
    mini = min(arr[sx][sy], arr[sx + 1][sy])
    temp = arr[sx][sy]
    arr[sx][sy] = arr[sx + 1][sy]
    visited = [[False] * len(arr[0]) for _ in range(len(arr))]

    q = deque([[sx, sy]])

    visited[sx][sy] = True
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    directions = deque(directions)
    dx, dy = directions.popleft()
    while q:
        x, y = q.popleft()

        nx = x + dx
        ny = y + dy

        if sx <= nx <= fx and sy <= ny <= fy:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny])
                if arr[nx][ny] < mini:
                    mini = arr[nx][ny]
                change = arr[nx][ny]
                arr[nx][ny] = temp
                temp = change
        else:
            if directions:
                dx, dy = directions.popleft()
                q.append([x, y])

    return mini, arr


def solution(rows, columns, queries):
    answer = []

    arr = [[i + columns * j for i in range(1, columns + 1)] for j in range(rows)]

    for q in queries:
        sx, sy, fx, fy = q
        sx -= 1
        sy -= 1
        fx -= 1
        fy -= 1
        mini, arr = rotate(sx, sy, fx, fy, arr)
        answer.append(mini)

    return answer