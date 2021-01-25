# https://www.acmicpc.net/problem/13549
import sys
input = sys.stdin.readline
from collections import deque

def bfs(start,target):
    dist = [-1] * (10**5+1)
    dist[start] = 0
    time = 0
    q = deque([start])
    while q:
        x = q.popleft()

        for nx in [2*x, x+1, x-1]:
            if 0<=nx<100001 and nx == 2*x and dist[nx] == -1:
                dist[nx] = dist[x]
                q.appendleft(nx)
            elif 0<=nx<100001 and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
    return dist[target]


start, target = map(int,input().split())
print(bfs(start,target))