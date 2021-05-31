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

"""
dp의 최대값은 
"""
maxi = 0

result = 0
for idx in range(N):
    if idx + days[idx] <= N:
        next_idx = idx + days[idx]
        dp[next_idx] = max(dp[idx] + costs[idx], dp[next_idx], maxi+costs[idx])

        if maxi < dp[idx]:
            maxi = dp[idx]

print(max(dp))