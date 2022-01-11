import sys
input = sys.stdin.readline
from collections import defaultdict, deque


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B_dict = defaultdict(int)
for i in B:
    B_dict[i] += 1

answer = 0
for i in range(100, -1, -1):
    while B_dict[i]:
        answer += A.pop() * i
        B_dict[i] -= 1

print(answer)