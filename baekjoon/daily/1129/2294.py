import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

# print(coins)

dp = [0] * (k+1)

for i in range(1, k+1):
    s = []
    for j in coins:
        if i-j >= 0 and dp[i-j] != -1:
            s.append(dp[i-j])

    if not s:
        dp[i] = -1
    else:
        dp[i] = min(s) + 1

print(dp[-1])