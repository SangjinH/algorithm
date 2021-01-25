# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE
# 격자판의 숫자 이어붙이기
from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

total = []

def bfs(graph, start_x, start_y, cnt):
    q = deque([(start_x, start_y)])
    nums = []
    nums.append(graph[start_x][start_y])

    while cnt < 6:
        cnt += 1
        x = start_x
        y = start_y

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 4 and 0 <= ny < 4:
                bfs(graph, nx, ny, cnt)
    total.append(nums)

n = int(input().rstrip())

arr = []
for _ in range(n):
    for _ in range(4):
        arr.append(list(map(int, input().rstrip().split())))


for i in range(4):
    for j in range(4):
        bfs(arr, i, j, 1)

print(total)