import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

infos = []
for _ in range(N):
    p, d = map(int, input().split())
    infos.append([p, d])

infos.sort(reverse=True)
infos = deque(infos)

check = [False]*10001

ans = 0
while infos:
    p, d = infos.popleft()
    if not check[d]:
        check[d] = True
        ans += p
    else:
        for i in range(d, 0, -1):
            if not check[i]:
                check[i] = True
                ans += p
                break

print(ans)
