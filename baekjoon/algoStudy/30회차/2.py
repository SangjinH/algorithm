"""

"""

import sys
input = sys.stdin.readline
from collections import deque


# locations = [1000000] * 100001
# routes = [[] for _ in range(100001)]

N, K = map(int, input().split())

q = deque()
q.append(N)

visited = [0] * 100001
path = [0] * 100001

while q:
    now = q.popleft()

    if now == K:
        print(visited[now])
        answer = []
        answer.append(K)

        while now != N:
            answer.append(path[now])
            now = path[now]

        answer.reverse()
        print(*answer)
        break


    for next in [now+1, now-1, now*2]:
        if 0 <= next < 100001 and not visited[next]:
            visited[next] = visited[now] + 1
            q.append(next)
            path[next] = now



