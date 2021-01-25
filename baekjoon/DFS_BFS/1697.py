# # https://www.acmicpc.net/problem/1697
# # 백준 1697번 , BFS, DFS 숨바꼭질
# import sys
# input = sys.stdin.readline
# from collections import deque
#
# n, k = map(int, input().rstrip().split())
#
#
# total = []
# range_list = [n]
# total.append(range_list)
# while True:
#
#     tmp = []
#     for i in range_list:
#         tmp.append(i-1)
#         tmp.append(i+1)
#         tmp.append(i*2)
#     total.append(tmp)
#     range_list = tmp
#
#     if k in tmp:
#         break
#
#
# if n == k:
#     print(0)
# else:
#     print(len(total)-1)

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().rstrip().split())

d = [0] * 100001

q = deque([n])

while True:
    num = q.popleft()

    if num == k:
        break
    if 0 <= num - 1 <= 100000 and d[num - 1] == 0:
        d[num - 1] = d[num] + 1
        q.append(num - 1)
    if 0 <= num + 1 <= 100000 and d[num + 1] == 0:
        d[num + 1] = d[num] + 1
        q.append(num + 1)
    if 0 <= num * 2 <= 100000 and d[num * 2] == 0:
        d[num * 2] = d[num] + 1
        q.append(num * 2)

print(d[k])
