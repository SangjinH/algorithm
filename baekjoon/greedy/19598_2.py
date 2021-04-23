import sys
input = sys.stdin.readline

N = int(input())
times = []

for _ in range(N):
    a, b = map(int, input().split())
    times.append((a, b))


times.sort()

print(times)

start = times[0][0]
end = times[0][1]
cnt = 1

# for time in times[1:]:
#     next_start = time[0]
#     next_end = time[1]
#
#     if next_start < end:
#        cnt += 1
# 4
# 5 10
# 0 10
# 10 15
# 10 30