import sys
input = sys.stdin.readline
from pprint import pprint

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
# 시작점 초기화
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        # 갈 수 있는 길이라면
        if arr[i][j] == 0:
            break

        if dp[i][j] != 0:
            dist = arr[i][j]
            if i + dist < N:
                dp[i+dist][j] += dp[i][j]

            if j + dist < N:
                dp[i][j+dist] += dp[i][j]

print(dp[-1][-1])