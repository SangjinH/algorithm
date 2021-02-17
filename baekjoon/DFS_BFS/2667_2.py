import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(arr, x, y):
    q = deque([(x, y)])
    arr[x][y] = 0
    

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input().split()))
