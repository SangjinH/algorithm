import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

vips = [0]
for _ in range(M):
    vips.append(int(input()))
vips.append(N+1)

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1
for i in range(1, len(vips)):
    answer *= dp[vips[i] - vips[i-1] - 1]

print(answer)