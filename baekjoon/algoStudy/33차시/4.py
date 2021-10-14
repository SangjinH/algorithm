import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
locates = []
parents = {i:i for i in range(n)}


def find(x):
    if x != parents[x]:
        return find(parents[x])
    return x


def union(a, b):
    a, b = find(a), find(b)
    for key in parents.keys():
        if parents[key] == max(a, b):
            parents[key] = min(a, b)


for _ in range(n):
    locates.append(list(map(int, input().split())))

for _ in range(m):
    a, b = map(int, input().split())
    union(a-1, b-1)


def dist(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**1/2

q = []
for i in range(len(locates)):
    for j in range(i+1, len(locates)):
        heapq.heappush(q, (dist(locates[i], locates[j]), i, j))

answer = 0
while q:
    distance, a, b = heapq.heappop(q)
    if parents[a] != parents[b]:
        answer += distance
        union(a, b)
        # print(parents)


print('{:.2f}'.format(answer))