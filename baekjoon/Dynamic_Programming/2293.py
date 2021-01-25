# https://www.acmicpc.net/problem/2293
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * 10001
dp[0] = 1
coins.sort()

for i in coins:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])