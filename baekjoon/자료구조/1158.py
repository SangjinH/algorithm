from collections import deque
import sys
input = sys.stdin.readline


N, K = list(map(int, input().split()))

num_list = deque(list(range(1, N+1)))

print('<', end='')
while len(num_list) > 1:

    for _ in range(K-1):
        tmp = num_list.popleft()
        num_list.append(tmp)

    print(num_list.popleft(), end=', ')

print(num_list[0], end='>')