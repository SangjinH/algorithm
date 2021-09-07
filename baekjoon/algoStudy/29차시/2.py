import sys
from pprint import pprint

input = sys.stdin.readline

"""
볼륨은 무조건 바꾸고 시작
V[i] 는 i 번째 곡을 연주하기전에 바꿀 수 있는 볼륨
N 곡의개수
S 시작볼륨
M : 최대 볼륨
"""


N, S, M = map(int, input().split())
V = list(map(int, input().split()))


dp = [[False] * (M+1) for _ in range(N+1)]
dp[0][S] = True


for i in range(N):
    for j in range(M+1):
        if dp[i][j]:
            if j + V[i] <= M:
                dp[i+1][j+V[i]] = True

            if j - V[i] >= 0:
                dp[i+1][j-V[i]] = True

flag = -1
for i in range(M, -1, -1):
    if dp[N][i]:
        flag = j
        break

print(flag)














#
# answer = 0
#
#
# def dfs(volume, index):
#     global answer
#
#     if volume > M or volume < 0:
#         return
#     if index == len(V):
#         answer = max(answer, volume)
#         return
#
#     dfs(volume+V[index], index+1)
#     dfs(volume-V[index], index+1)
#
#
# dfs(S, 0)
# if answer == 0:
#     print(-1)
# else:
#     print(answer)


