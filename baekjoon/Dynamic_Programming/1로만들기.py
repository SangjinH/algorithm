from collections import deque

X = int(input())

dp = [0] * (X+1)

q = deque([X])
while q:
    now = q.popleft()

    if now % 5 == 0 and dp[now//5] == 0:
        dp[now//5] = dp[now] + 1
        q.append(now//5)

    if now % 3 == 0 and dp[now // 3] == 0:
        dp[now // 3] = dp[now] + 1
        q.append(now//3)

    if now % 2 == 0 and dp[now // 2] == 0:
        dp[now // 2] = dp[now] + 1
        q.append(now//2)

    if now - 1 > 0 and dp[now-1] == 0:
        dp[now-1] = dp[now] + 1
        q.append(now-1)

    if dp[1] != 0:
        break

print(dp)
print(dp[1])