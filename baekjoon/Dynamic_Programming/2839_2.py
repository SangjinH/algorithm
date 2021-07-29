import sys
input = sys.stdin.readline

n = int(input())

dp = [-1] * (5001)


dp[3] = 1
dp[5] = 1

for i in range(6, 5001):
    mini = 5000
    if dp[i-3] != -1:
        mini = min(dp[i-3], mini)

    if dp[i-5] != -1:
        mini = min(dp[i-5], mini)

    if mini != 5000:
        dp[i] = mini + 1

# print(dp)
print(dp[n])