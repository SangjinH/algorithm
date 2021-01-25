# https://www.acmicpc.net/problem/14501
# 백준 14501, DP , 퇴사

import sys
input = sys.stdin.readline


n = int(input().rstrip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

day = []
pay = []
for i in range(n):
    day.append(arr[i][0])
    pay.append(arr[i][1])

dp = [0] * (n+1)

for i in range(n):
    if i + day[i] <= n:
        dp[i] = pay[i]
print(day)
print(dp)

for i in range(n):
    if i + day[i] <= n:
        dp[i] = max(pay[i] + dp[i+day[i]], dp[i+1])

print(dp)