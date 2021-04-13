import sys
input = sys.stdin.readline
from collections import defaultdict

N, R, Q = list(map(int, input().split()))

tree = defaultdict(list)


for _ in range(N-1):
    a, b = list(map(int, input().split()))
    tree[a].append(b)
    tree[b].append(a)


