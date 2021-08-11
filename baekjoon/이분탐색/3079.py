import sys
input = sys.stdin.readline

n, m = map(int, input().split())

times = []
now = [0] * n
for _ in range(n):
    times.append(int(input()))

# 최소시간은 1, 최대시간은 사람 수 * 최소시간
mini = 1
maxi = min(times)*m

result = 0

while mini <= maxi:

    mid = (mini+maxi) // 2

    cnt_people = 0
    for t in times:
        cnt_people += mid // t

    if cnt_people >= m:
        maxi = mid - 1
        result = mid

    else:
        mini = mid + 1

print(result)