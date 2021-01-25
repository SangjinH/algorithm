# https://www.acmicpc.net/problem/9461
# 백준 알고리즘 9461번 , 파도반 수열
import sys
input = sys.stdin.readline

d = [0] * 101
d[0] = 1
d[1] = 1
d[2] = 1
for i in range(3,len(d)):
    d[i] = d[i-2] + d[i-3]

n = int(input().rstrip())
for _ in range(n):
    print(d[int(input().rstrip())-1])
