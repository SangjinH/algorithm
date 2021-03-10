import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(N):
    for j in range(1, N):
        arr[i][j] += arr[i][j-1]

for i in range(N):
    for j in range(1, N):
        arr[j][i] += arr[j-1][i]

print(arr)

for i in range(M):
    x1, y1, x2, y2 = list(map(int, input().split()))


    ans = arr[x2][y2] - arr[x1][y2] - arr[x2][y1] + arr[x1][y1]
    print(ans)