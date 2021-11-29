import sys
input = sys.stdin.readline
from collections import deque
"""
처음으로는 1번 풍선을 터뜨림
그 숫자만큼 이동해서 걔를 터뜨린다.

"""

N = int(input())
nums = list(map(int, input().split()))

q = deque()
for i in range(len(nums)):
    q.append([i+1, nums[i]])


while q:
    now = q.popleft()
    print(now[0], end=" ")

    if not q:
        break

    if now[1] > 0:
        for _ in range(now[1]-1):
            head = q.popleft()
            q.append(head)

    else:
        for _ in range(abs(now[1])):
            tail = q.pop()
            q.insert(0, tail)
