# 백준 1744 수묶기 , greedy
import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

positives = []
negatives = []
zeros = 0
ans = 0
for i in range(n):
    if i <= 0:
        negatives.append(i)
    elif i == 1:
        ans += 1
    else:
        positives.append(i)

negatives.sort()
positives.sort(reverse=True)

for i in range(0,len(negatives),2):
    if i+1 < len(negatives):
        ans += negatives[i]*negatives[i+1]
    else:
        ans += negatives[i]

for i in range(0, len(positives), 2):
    if i+1 < len(positives):
        ans += positives[i] + positives[i+1]
    else:
        ans += positives[i]

print(ans)