# https://www.acmicpc.net/problem/11727
# 백준 11727, DP 2Xn 타일링
import sys

input = sys.stdin.readline

# 세로
# 가로 둘
# 정사각형 1개

n = int(input().rstrip())

d = [0] * (n+1)

d[0] = 1
d[1] = 1

for i in range(2,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n]%10007)