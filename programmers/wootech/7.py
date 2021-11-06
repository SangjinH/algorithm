def dfs(x, y, directions, arr, visited, clockwise):
    temp = ['', '']
    next = []
    for i in range(len(directions)):
        nx = x + directions[i][0]
        ny = y + directions[i][1]

        if arr[nx][ny] != '' and not visited[nx][ny]:
            visited[nx][ny] = True
            temp[i] = arr[nx][ny]

            if clockwise:
                if ny+1 < len(arr[0]) and arr[nx][ny+1] != '':
                    next.append([nx, ny+1])
            else:
                if ny-1 >= 0 and arr[nx][ny-1] != '':
                    next.append([nx, ny-1])

    return temp, next


def rotate(arr, clockwise):

    visited = [[False]*len(arr[0]) for _ in range(len(arr))]
    temp = []

    directions = [[[0, 1], [-1, 0]], [[-1, 0], [0, -1]]]

    # 시계 방향 회전
    if clockwise:
        temp.append(arr[-1][0])
        visited[-1][0] = True
        start = [len(arr)-1, 1]
        idx = 0
        # 확인 순서 == 오른쪽, 위쪽

    # 반시계 방향 회전
    else:
        temp.append(arr[-1][-1])
        visited[-1][-1] = True
        start = [len(arr)-1, len(arr[-1])-2]
        idx = 1
        # 확인 순서 == 위쪽, 왼쪽

    candidates = [start]
    subs = []
    while candidates:
        next_one = ''
        for i in candidates:
            x, y = i
            nums, next = dfs(x, y, directions[idx], arr, visited, clockwise)
            next_one += nums[0] + arr[x][y] + nums[1]
            for j in next:
                subs.append(j)

        candidates = subs
        temp.append(next_one)
        subs = []
    return temp


def solution(grid, clockwise):

    N = len(grid[-1])
    arr = [[""] * N for _ in range(len(grid))]

    for i in range(len(grid)):
        temp = ((N-len(grid[i]))//2)
        for j in range(len(grid[i])):
            arr[i][temp+j] = grid[i][j]

    return rotate(arr, clockwise)


print(solution(["1","234","56789"], 'true'))
print(solution(["A","MAN","DRINK","WATER11"], 'false'))
