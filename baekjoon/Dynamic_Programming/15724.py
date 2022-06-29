import sys
input = sys.stdin.readline

N, M = map(int, input().split())


arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, N):
    arr[0][i] += arr[0][i-1]

for j in range(1, M):
    arr[j][0] += arr[j-1][0]


for i in range(1, N):
    for j in range(1, M):
        arr[i][j] += (arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1])

# print(arr)

K = int(input())
points = []
for _ in range(K):
    a, b, c, d = map(int, input().split())
    print(arr[c-1][d-1] - arr[a-2][b-1] - arr[a-1][b-2] + arr[a-2][b-2])
