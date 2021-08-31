import sys
input = sys.stdin.readline

# 가장 긴 증가하는 부분수열의 문제

nums = []

n = int(input())
for _ in range(n):
    nums.append(int(input()))

dp_max = 0

dp = [1] * len(nums)

for i in range(1, len(nums)):

    maxi = 0
    for j in range(i, -1, -1):
        if nums[j] < nums[i]:
            if dp[j] > maxi:
                maxi = dp[j]
    dp[i] += maxi

    if dp[i] > dp_max:
        dp_max = dp[i]

print(len(nums)-dp_max)


