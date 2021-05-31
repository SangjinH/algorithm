from collections import deque
from pprint import pprint

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def find_another(p_list, place):
    for p in p_list:
        visited = [[False]*5 for _ in range(5)]
        cnt = 0
        visited[p[0]][p[1]] = 1
        temp = [p]
        while cnt < 2:
            next_check = []
            for i in temp:
                x = i[0]
                y = i[1]

            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nx = x + dx
                ny = y + dy

                # 범위 내에있고 가지않은 길이라면
                if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                    # P를 만나면
                    if place[nx][ny] == 'P':
                        return 0
                    # 갈 수 있는 길이라면
                    elif place[nx][ny] == 'O':
                        next_check.append((nx, ny))

            cnt += 1
            temp = next_check
    return 1




def solution(places):
    result = []
    for place in places:
        p_list = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p_list.append((i, j))
        result.append(find_another(p_list, place))
    return result

print(solution(places))