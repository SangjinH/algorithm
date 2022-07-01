import sys
input = sys.stdin.readline

# 준서가 얻을 수 있는 가치의 최댓값을 알아보자
# 하나하나씩 비교하면서, 현재 최고 가치를 기준으로 무게를 더한 값과 비교해서 더 높다면 바꾸기


N, K = map(int, input().split())

dp = [0]*(K+1)

for i in range(1, N+1):

    W, V = map(int, input().split())

    for j in range(K, W-1, -1):
        dp[j] = max(dp[j], dp[j-W]+V)

print(dp[-1])