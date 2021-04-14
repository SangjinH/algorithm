import sys
input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))
dp = num_list[:]

for i in range(1, N):
    if num_list[i] + dp[i-1] >= 0:
        dp[i] = max(dp[i], num_list[i] + dp[i-1])

print(max(dp))