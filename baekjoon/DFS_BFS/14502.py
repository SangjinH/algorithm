# 백준 14502
import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
arr = []
virus_list = []
clean = []
for _ in range(n):
    arr.append(list(map(int,input().rstrip().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus_list.append((i,j))
        if arr[i][j] == 0:
            clean.append((i,j))

comb_list = list(combinations(clean,3))

# print(comb_list)
# # print(virus_list)
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

def bfs(a,b):
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0 <= nx < n and 0 <= ny < m and arr2[nx][ny] == 0:
            arr2[nx][ny] = 2
            bfs(nx, ny)

cnt_list = []

for i in comb_list:
    arr2 = copy.deepcopy(arr)
    # print(arr2)
    arr2[i[0][0]][i[0][1]] = 1
    arr2[i[1][0]][i[1][1]] = 1
    arr2[i[2][0]][i[2][1]] = 1

    # p.pprint(arr2)
    for i in virus_list:
        a, b = i
        bfs(a,b)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 0:
                cnt += 1
    cnt_list.append(cnt)
print(max(cnt_list))