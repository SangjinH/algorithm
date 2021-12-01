import sys
input = sys.stdin.readline

"""
공유기 설치,
한 집에 하나의 공유기를 설치하고,
인접한 두 공유기 사이의 거리를 가능한 크게
"""

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

s = 1
e = houses[-1]

answer = (s+e)//2
while s <= e:
    m = (s+e)//2

    cnt = 1
    start = houses[0]
    for i in range(1, len(houses)):
        if houses[i] - start >= m:
            cnt += 1
            start = houses[i]

    # 설치 갯수보다 많이 설치했다 == 거리가 짧다.
    if cnt >= C:
        s = m + 1
        answer = m

    elif cnt < C:
        e = m - 1

print(answer)