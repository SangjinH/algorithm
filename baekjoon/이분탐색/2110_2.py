import sys
input = sys.stdin.readline


n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))

houses.sort()

# 사이의 거리의 최소, 최대값
mini = 1
maxi = houses[-1] - houses[0]

result = 0

while mini <= maxi:
    mid = (mini + maxi) // 2

    old = houses[0]
    cnt = 1

    for i in range(1, len(houses)):
        if houses[i] >= old + mid:
            cnt += 1
            old = houses[i]
    # 찾은 갯수가 공유기 갯수보다 같거나 많다면
    if cnt >= c:
        mini = mid + 1
        # 결과에 저장
        result = mid
    # 더 적다면
    else:
        # 거리 좁히기
        maxi = mid-1


print(result)
