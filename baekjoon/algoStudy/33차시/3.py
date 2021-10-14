import sys
input = sys.stdin.readline


n = int(input())

one_nums = []

num = 0
idx = 1
while num < n:
    num += idx * (idx+1) // 2
    one_nums.append(num)
    idx += 1

INF = int(1e9)
dp = [INF] * (n+1)

for i in range(1, n+1):
    for num in one_nums:
        if num == i:
            dp[i] = 1
            break

        if num > i:
            break

        dp[i] = min(dp[i], dp[i-num]+1)

print(dp[-1])