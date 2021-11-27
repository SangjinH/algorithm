import sys
input = sys.stdin.readline

n = int(input())

doubles = []
for i in range(1, int(n**(1/2))+1):
    doubles.append(i**2)

dp = [0] * (n+1)

for i in doubles:
    dp[i] = 1

for i in range(1, n+1):
    temp = []
    for j in doubles:
        if i-j < 0:
            break
        temp.append(dp[i-j])

    dp[i] = min(temp)+1

print(dp[-1])