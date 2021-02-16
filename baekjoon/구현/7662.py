import sys
input = sys.stdin.readline
import heapq

T = int(input())

for _ in range(T):
    K = int(input())

    q = []
    for _ in range(K):
        word, num = list(input().split())
        num = int(num)

        if word == 'I':
            heapq.heappush(q, num)
        else:
            if not len(q):
                continue
            if num == 1:
                q = q[:-1]
            else:
                q = q[1:]
    if not q:
        print('EMPTY')
    else:
        print(q[-1], q[0])