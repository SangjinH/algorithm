import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
plane = []
for _ in range(P):
    plane.append(int(input()))

def parent_find(x):
    if x == parent[x]:
        return x
    # 이 부분이 무슨말이지 ??
    p = parent_find(parent[x])
    parent[x] = p
    return parent[x]


def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    parent[x] = y


# parent[0] = 0 까지 만들어준다. parent[x] = 0까지 만들어지는게 핵심!
parent = {i:i for i in range(G+1)}
cnt = 0
for i in plane:
    x = parent_find(i)
    if x == 0:
        break
    union(x, x-1)
    cnt += 1

print(cnt)