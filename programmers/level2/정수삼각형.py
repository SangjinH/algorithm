def solution(triangle):
    total = triangle[0][0]
    dp = triangle

    if len(triangle) == 1:
        return total

    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            temp = []
            if j - 1 >= 0:
                temp.append(dp[i - 1][j - 1])
            if j < len(dp[i - 1]):
                temp.append(dp[i - 1][j])

            dp[i][j] = max(temp) + dp[i][j]

    return max(dp[-1])