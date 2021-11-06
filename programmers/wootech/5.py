from collections import deque

def solution(rows, columns):

    arr = [[0]*columns for _ in range(rows)]
    check = [[[0,0] for _ in range(columns)] for _ in range(rows)]

    directions = [[0, 1], [1, 0]]
    idx = 0
    arr[0][0] = 1
    check[0][0][idx] = 1
    q = deque([(0, 0)])
    cnt = 1

    while q:
        x, y = q.popleft()
        dx, dy = directions[idx]
        nx = (x + dx) % rows
        ny = (y + dy) % columns
        idx = abs(1-idx)
        if check[nx][ny][idx]:
            break
        if arr[nx][ny] == 0:
            cnt += 1

        arr[nx][ny] = arr[x][y] + 1
        if cnt == rows * columns:
            break
        q.append((nx, ny))

    return arr



print(solution(3, 4))
print(solution(3, 3))
print(solution(3, 6))