# https://www.acmicpc.net/problem/13549
from collections import deque
import sys
input = sys.stdin.readline

start, target = map(int, input().split())

dist = [-1] * (10**5+1)


q = deque([start])
while q:
    num, time = q.popleft()

    if num == target:
        print(time)
        break
    q.append((num+1, time+1))
    q.append((num-1, time+1))
    q.append((num*2, time))
