# https://www.acmicpc.net/problem/2110
# 공유기 설치

import sys
input = sys.stdin.readline

"""
총 공유기 C 개를 설치,
한 집에 공유기 하나 설치, 
가장 인접한 두 공유기 사이의 거리를 가장 크게 

예제
5 3
1
2
8
4
9
"""


n, c = map(int, input().split())

houses = []
for _ in range(n):
    houses.append(int(input()))

houses.sort()

# 좌표의 최소값
start = 1

# 가장 높은 좌표와 가장 낮은 좌표의 차이
end = houses[-1] - houses[0]

result = 0

while start <= end:
    mid = (start + end) // 2
    old = houses[0]
    cnt = 1

    for i in range(1, len(houses)):
        if houses[i] >= old + mid: # gap 이상이면
            cnt += 1
            old = houses[i]
            print("old : ", old)

    if cnt >= c:
        start = mid + 1
        result = mid
        print("start", start)
        print("end ", end)
        print("result", result)
        print("mid : ", mid)
        print()

    else:
        end = mid - 1

print(result)