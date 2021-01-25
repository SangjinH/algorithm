# 백준 2839번, 설탕배달
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())

cnt = 0
mock_5 = n // 5
min_value = INF

for i in range(0, mock_5+1):
    cnt = i
    num = n - 5*cnt
    # print(num)

    if num % 3 == 0:
        cnt += num // 3
        min_value = min(cnt, min_value)

if min_value == INF:
    print(-1)
else:
    print(min_value)