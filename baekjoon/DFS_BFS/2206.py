# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기
import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(start):



N, M = list(map(int, input().split()))
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
print(visited)