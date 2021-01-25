import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

networks = [[] for _ in range(n + 1)]

for _ in range(int(input().rstrip())):
    a, b = map(int, input().rstrip().split())
    networks[a].append(b)
# print(networks)

start = 1
q = deque([start])

visited = []
while q:
    v = q.popleft()
    visited.append(v)
    for i in networks[v]:
        if i not in visited:
            q.append(i)
            visited.append(i)

print(len(set(visited))-1)