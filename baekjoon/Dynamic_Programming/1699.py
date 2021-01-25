# https://www.acmicpc.net/problem/1699
import sys
input = sys.stdin.readline

doubles = []

cnt = 1
while True:
    if cnt ** 2 <= 100000:
        doubles.append(cnt**2)
    else:
        break
    cnt += 1
k = int(input())

dp = [0 for x in range(k+1)]

for i in range(1, k+1):
    temp = []
    for j in doubles:
        if i - j < 0:
            break
        else:
            temp.append(dp[i-j])
    dp[i] = min(temp)+1

print(dp[k])