import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())

result = []
for i in range(N):
    num, name = list(input().split())
    result.append([int(num), name, i])

result.sort(key=lambda x: [x[0], x[2]])

for i in result:
    print(i[0],i[1])