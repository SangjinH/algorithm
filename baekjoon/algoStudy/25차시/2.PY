import sys
input = sys.stdin.readline

# def parent_find(x):
#     # 자기자신이 곧 부모라면 return
#     if x == p[x]:
#         return x
#
#     parent = parent_find(p[x])
#     p[x] = parent
#     return p[x]
#
#
# def union(x, y):
#     x = parent_find(x)
#     y = parent_find(y)
#     if x < y:
#         p[y] = x
#     else:
#         p[x] = y

### 2 재귀
def dfs(x):
    visited[x] = True
    next = nums[x]
    if not visited[next]:
        dfs(next)


T = int(input())

for _ in range(T):
    n = int(input())
    nums = [0] + list(map(int, input().split()))

    visited = [False] * (len(nums)+1)
    ans = 0
    for i in range(1, len(nums)):
        if not visited[i]:
            dfs(i)
            ans += 1

    print(ans)