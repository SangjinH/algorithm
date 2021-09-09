import sys
input = sys.stdin.readline

n, k = map(int, input().split())

"""
n 이라고 했을때
될 수 있는 것 라인업
1, n-1
2, n-2
3, n-3
...
n-3, 3
n-2, 2
n-1, 1
"""


def count(x):
    return (x+1)*(n-x+1)


lo = 0
hi = n//2 + 1

while lo < hi:
    mid = (lo + hi) // 2
    if count(mid) == k:
        print("YES")
        sys.exit(0)
    elif count(mid) > k:
        hi = mid
    elif count(mid) < k:
        lo = mid + 1

print("NO")