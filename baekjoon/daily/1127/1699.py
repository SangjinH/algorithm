import sys
input = sys.stdin.readline


n = int(input())
doubles = []
for i in range(1, int(n**(1/2))+1):
    doubles.append(i**2)

dp = [0] * (n+1)

for i in doubles:
    dp[i] = 1


for i in range(1, len(dp)):
    # DP의 값이 있다면
    if dp[i]:
        for j in doubles:
            temp = dp[i] + 1
            if i+j < len(dp):
                if not dp[i+j]:
                    dp[i+j] = temp
                else:
                    dp[i+j] = min(dp[i+j], temp)
print(dp)
print(dp[-1])