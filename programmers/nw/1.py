directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

from collections import deque


def dfs(x, y, idx, curr_num, lengths, n, arr):
    global directions

    if len(lengths) == 1:
        q = deque()
        q.append([x, y])
        arr[x][y] = curr_num
        turn_cnt = 0

        while q:
            if turn_cnt >= 2:
                break

            now_x, now_y = q.popleft()

            nx = now_x + directions[idx][0]
            ny = now_y + directions[idx][1]

            # 범위 내에 있다면
            if x <= nx < x + n // lengths[-1] and y <= ny < y + n // lengths[-1]:
                if not arr[nx][ny]:
                    arr[nx][ny] = curr_num
                    curr_num += 1
                    q.append([nx, ny])
                    turn_cnt = 0
                else:
                    turn_cnt += 1
                    idx = (idx + 1) % 4
                    q.append([now_x, now_y])
            else:
                turn_cnt += 1
                idx = (idx + 1) % 4
                q.append([now_x, now_y])
        return curr_num, arr

    else:
        visited = [[False] * n for _ in range(n)]

        q = deque()
        q.append([x, y])
        visited[x][y] = True
        turn_cnt = 0

        while q:
            if turn_cnt >= 2:
                break

            now_x, now_y = q.popleft()

            nx = now_x + directions[idx][0] * (n // lengths[-1])
            ny = now_y + directions[idx][1] * (n // lengths[-1])

            print(nx, ny, 'adsfasd', n, "n", lengths)
            print(visited)
            if x <= nx < x + n and y <= ny < y + n:
                if not visited[nx][ny]:
                    # 방문처리, 그 속에 들어가서 dfs
                    visited[nx][ny] = True
                    curr, arr = dfs(nx, ny, 0, curr_num, lengths[:-1], n // lengths[-1], arr)
                    q.append([nx, ny])
                    turn_cnt = 0
                else:
                    turn_cnt += 1
                    idx = (idx + 1) % 4
                    q.append([now_x, now_y])
            else:
                print("turnturn", nx, ny)
                turn_cnt += 1
                idx = (idx + 1) % 4
                q.append([now_x, now_y])

    return curr_num


def solution(lengths):

    n = 1
    for i in lengths:
        n *= i

    print(n)

    arr = [[0] * n for _ in range(n)]



    dfs(0, 0, 0, 1, lengths, n, arr)

    print(arr)



print(solution([3, 2]))
print(solution([2, 3]))
print(solution([2, 2, 2]))
