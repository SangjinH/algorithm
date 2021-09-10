"""
맨해튼 거리 2 이하
P : 응시자가 않은 자리
O : 빈 테이블
X : 파티션
"""

from collections import deque

def bfs(x, y, place):
    q = deque()
    q.append([x, y, 0])
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True

    while q:
        x, y, dist = q.popleft()

        if dist == 2:
            continue

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy

            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and dist <= 2:
                if place[nx][ny] == "O":
                    visited[nx][ny] = True
                    q.append([nx, ny, dist+1])
                elif place[nx][ny] == "X":
                    continue
                else:
                    if place[nx][ny] == "P":
                        return False
    return True




def solution(places):

    answer = []
    for place in places:
        p_list = []

        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if not bfs(i, j, place):
                        print(place, i, j)
                        flag = False
                        break
            if not flag:
                break

        if not flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
