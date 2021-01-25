# 백준 1475 , 구현
import sys
from collections import deque

input = sys.stdin.readline

num_count = [1, 1, 1, 1, 1, 1, 2, 1, 1, 2]
num_info = [0]*10

n = int(input().rstrip())

for i in range(len(str(n))):
    num_info[int(str(n)[i])] += 1

num_info[6] = num_info[6] + num_info[9]

q = deque(num_info)
q.pop()
for i in range(len(q)):
    if i == 6:
        q[i] = round(q[i]/2)

print(max(q))