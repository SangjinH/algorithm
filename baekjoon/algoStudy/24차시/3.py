import sys
input = sys.stdin.readline

num, e, w, s, n = map(int, input().split())

p = [e/100, w/100, s/100, n/100]
ans = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, visited, prob):
    global ans

    if len(visited) == num + 1:
        ans += prob
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, visited, prob*p[i])
            visited.pop()

dfs(0, 0, [(0, 0)], 1)

print(ans)