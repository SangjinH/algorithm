import sys
input = sys.stdin.readline

N = int(input())

days = []
costs = []
for _ in range(N):
    d, c = map(int, input().split())
    days.append(d)
    costs.append(c)

dp = [0] * (N+1)

if days[0] < N:
    dp[days[0]] += costs[0]

for idx in range(1, N):
    if idx + days[idx] <= N:
        comp_day = idx + days[idx]
        dp[comp_day] = max(max(dp[:idx+1]) + costs[idx], dp[comp_day])

print(max(dp))