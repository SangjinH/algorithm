# https://www.acmicpc.net/problem/15686
# 백준 15686, 구현
import sys
input = sys.stdin.readline
from itertools import combinations
INF = int(1e9)

n, m = map(int, input().rstrip().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

cases = list(combinations(chickens, m))
# print(cases)

results = []
for c in cases:
    # print(c)
    d = [INF] * len(houses)
    for j in range(len(c)):
        for k in range(len(houses)):
            d[k] = min(d[k], abs(houses[k][0]-c[j][0])+abs(houses[k][1]-c[j][1]))
    results.append(sum(d))
print(min(results))