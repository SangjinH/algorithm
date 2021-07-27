# https://www.acmicpc.net/problem/21317

import sys
input = sys.stdin.readline


# N 개의 돌이 있는데
# 마지막 돌 틈 사이에 산삼이 있음

# 점프 = 작은점프(1칸), 큰점프(2칸), 매우큰점프(3칸)

# 매우 큰 점프는 무조건 1번, 돌 번호와 상관없이 K 만큼 에너지소비

# 산삼을 얻기 위해 필요한 에너지의 최소값

# 1  2  4  6
# 2  3  5  7

# 총 3 가지 경우에서의 최솟값을 찾으면 된다.
# 매우 큰 점프는 4번 부터 체크해주면 된다.


n = int(input())

rocks = []

for _ in range(n-1):
    rocks.append(list(map(int, input().split())))

k = int(input())

# dp를 2차원으로 만들기 첫번째는 뛰지 않은 상태
# 두번째는 한번 뛰었을때
dp = [[0, 0] * n]

# dp 초기화 처음 1칸을 뛰는 경우는 무조건

if n > 3:
    dp[1] = rocks[0][0]
    dp[2] = min(dp[1]+rocks[1][0], rocks[0][1])
    dp[3] = min(dp[2]+rocks[2][0], dp[1]+rocks[1][1])

    for i in range(4, n):
        dp[i] = min(dp[i-1]+rocks[i-1][0], dp[i-2]+rocks[i-2][1], dp[i-3]+k)

    print(dp[-1])

elif n == 1:
    print(0)

elif n == 2:
    print(rocks[0][0])

elif n == 3:
    dp[1] = rocks[0][0]
    dp[2] = min(dp[1]+rocks[1][0], rocks[0][1])
    dp[3] = min(dp[2]+rocks[2][0], dp[1]+rocks[1][1])
    print(dp[-1])



