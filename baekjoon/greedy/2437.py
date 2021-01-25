# 백준 2437번, 그리디
from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input().rstrip())
s = list(map(int, input().split()))
s.sort()
num = 1
for i in range(n):
    if num < s[i]:
        break
    num += s[i]

print(num)