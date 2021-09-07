import sys
input = sys.stdin.readline

"""
거리는 유클리드거리

"""


M, N, L = map(int, input().split())

fires = list(map(int, input().split()))
fires.sort()

locs = []
for _ in range(N):
    x, y = map(int, input().split())
    locs.append([x, y])

# print(fires)
# print(locs)

answer = 0

for loc in locs:
    l = 0
    r = len(fires)-1
    while l<r:
        mid = (l+r) // 2
        if fires[mid] < loc[0]:
            l = mid + 1
        else:
            r = mid

    if abs(fires[r]-loc[0])+loc[1] <= L or abs(fires[r-1]-loc[0]) + loc[1] <= L:
        answer += 1

print(answer)