import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    visited = [-1] * 10000
    visited[n] = ''
    q = deque([n])

    while q:
        now = q.popleft()

        if now == B:
            return visited[now]

        no, nx = divmod(2*now, 10000)
        if visited[nx] == -1:
            visited[nx] = visited[now] + 'D'
            q.append(nx)

        if now == 0:
            nx = 9999
        else:
            nx = now-1

        if visited[nx] == -1:
            visited[nx] = visited[now] + 'S'
            q.append(nx)

        nx = (now%1000)*10 + now//1000
        if visited[nx] == -1:
            visited[nx] = visited[now] + 'L'
            q.append(nx)

        nx = (now%10)*1000 + now//10
        if visited[nx] == -1:
            visited[nx] = visited[now] + 'R'
            q.append(nx)


T = int(input())
for _ in range(T):
    A, B = list(map(int, input().split()))
    print(bfs(A))
