def solution(numOfStairs):
    dp = [[] for _ in range(numOfStairs+1)]

    if numOfStairs == 1:
        return 1
    dp[1] = 1

    if numOfStairs == 2:
        return 2
    dp[2] = 2

    if numOfStairs == 3:
        return 4
    dp[3] = 4

    for i in range(4, numOfStairs+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


    return dp[-1]

print(solution(4))