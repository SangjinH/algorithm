import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

dp = [0] * len(num_list)
dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if num_list[i] > num_list[j] and dp[i] < dp[j]:
            dp[i] = dp[j]

    dp[i] += 1

print(max(dp))