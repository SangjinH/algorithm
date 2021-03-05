import sys
input = sys.stdin.readline
from pprint import pprint

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def put_Q(cnt, arr):
    print('function call.. with cnt : ', cnt)
    global ans

    if cnt == N:
        ans += 1
        print(ans)
        return

    for x in range(N):
        for y in range(N):
            fall_back = []
            if not arr[x][y]:
                # print('check (x, y) : ', (x, y))
                arr[x][y] = True
                fall_back.append((x, y))
                cnt += 1
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    while 1:
                        if 0<=nx<N and 0<=ny<N and (not arr[nx][ny]):
                            arr[nx][ny] = True
                            fall_back.append((nx, ny))
                            nx += dx[i]
                            ny += dy[i]
                        else:
                            break

                print('temp: ',arr)
                print('arr')
                pprint(arr)

                put_Q(cnt, arr)

                for info in fall_back:
                    print(info)
                    arr[info[0]][info[1]] = False
                print('back_arr')
                pprint(arr)
                cnt -= 1





N = int(input())
visited = [[False]*N for _ in range(N)]
ans = 0
put_Q(0, visited)
print(ans)


