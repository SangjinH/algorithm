import sys
input = sys.stdin.readline

N = int(input())

times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x: x[1])

maxi = times[-1][-1]
check = [0]*maxi

for time in times:
    for i in range(time[0], time[1]):
        check[i] += 1

print(max(check))