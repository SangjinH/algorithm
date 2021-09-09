import sys
input = sys.stdin.readline
import heapq

"""
M 개의 휴게소를 더 지어 
휴게소가 없는 구간을 최소화 하고싶다. 
"""

N, M, L = map(int, input().split())
rests = list(map(int, input().split()))
rests.append(0)
rests.append(L-1)

rests.sort()

answer = 0

l = 0
r = L - 1
while l <= r:
    mid = ( l + r ) // 2
    count = 0
    for i in range(1, len(rests)):
        if rests[i] - rests[i-1] > mid:
            count += (rests[i] - rests[i-1] - 1) // mid

    if count > M:
        l = mid + 1
    else:
        answer = mid
        r = mid - 1

print(answer)