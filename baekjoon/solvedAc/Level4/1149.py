import sys
input = sys.stdin.readline


N = int(input())

costs = []
for _ in range(N):
    costs.append(list(map(int, input().split())))

