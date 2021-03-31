import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))

stuffs = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    stuffs.append((a, b))

dp = [0] * (K+1)

for i in stuffs:
    for j in range(K, i[0]-1, -1):
        dp[j] = max(dp[j], dp[j-i[0]]+i[1])

print(dp[-1])

