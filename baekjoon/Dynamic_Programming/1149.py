# https://www.acmicpc.net/problem/1149
# 백준 1149번 DP, RGB거리 색칠하기
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())

d = []
for _ in range(n):
    d.append(list(map(int, input().rstrip().split())))

for i in range(1,n):
    d[i][0] = d[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = d[i][1] + min(d[i-1][0], d[i-1][2])
    d[i][2] = d[i][2] + min(d[i-1][0], d[i-1][1])

print(min(d[n-1]))