def dp_Hamburger():
    dp = [0] * (L+1)

    for i in ingredients:
        for j in range(L, i[1]-1, -1):
            dp[j] = max(dp[j], i[0]+dp[j-i[1]])

    return dp[-1]

T = int(input())
for tc in range(1, T+1):
    N, L = list(map(int, input().split()))
    ingredients = []
    for _ in range(N):
        # [score, cal]
        ingredients.append(list(map(int, input().split())))

    print(f'#{tc} {dp_Hamburger()}')