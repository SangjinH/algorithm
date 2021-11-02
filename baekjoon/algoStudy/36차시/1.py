import sys
input = sys.stdin.readline

N, M = map(int, input().split())

check = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    check[a][b] = 1
    check[b][a] = 1



cnt = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        if check[i][j] or check[j][i]:
            continue
        for k in range(j+1, N+1):
            if check[i][k] or check[k][i] or check[j][k] or check[k][j]:
                continue
            cnt += 1
print(cnt)