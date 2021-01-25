# https://www.acmicpc.net/problem/3190
# 백준 3190번, 뱀
import sys
input = sys.stdin.readline
from collections import deque

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n = int(input())
arr = [[0]*n for _ in range(n)]

k = int(input())

for _ in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 1

directions = []
num = int(input())
for i in range(num):
    a, b = input().split()
    directions.append((int(a), b))

# print(arr)
cnt = 0
q = deque([(0,0)])
while True:
    x, y = q.popleft()
    arr[x][y] = 3
