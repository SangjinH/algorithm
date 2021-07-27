# 전깃줄이 교차하지 않게 없애야하는 최소 갯수
# 제일 많이 교차하는 것부터 없애는 게 맞나 ?

import sys
input = sys.stdin.readline

n = int(input())

lines = []

for _ in range(n):
    lines.append(list(map(int, input().split())))


lines.sort()

# 처음 dp값 초기화
dp = [[] for _ in range(n)]
dp[0].append([lines[0][1]])
min_value = lines[0][1]


for i in range(1, n):
    if min_value > lines[i][1]:
        dp[i].append([lines[i][1]])
        min_value = lines[i][1]
    # 전에 증가하는 항들을 보면서
    for j in dp[i-1]:
        dp[i].append(j)
        if j[-1] < lines[i][1]:
            temp = j + [lines[i][1]]
            dp[i].append(temp)

max_len = 0
for i in dp[-1]:
    if len(i) > max_len:
        max_len = len(i)


print(n-max_len)