import sys
input = sys.stdin.readline

N, practise = list(input().split())
playlist = [list(input().rstrip().split(':')) for _ in range(int(N))]
practise = practise.split(':')
minutes = [0]
N = int(N)

usable = int(practise[0])*3600 + int(practise[1])*60 + int(practise[2])

for time in playlist:
	minutes.append(int(time[0])*60 + int(time[1]))

for i in range(1, len(minutes)):
    minutes[i] += minutes[i-1]


ans = [0, 0]
for i in range(len(minutes)):
    standard = minutes[i]
    cnt = 0
    for j in range(i+1, len(minutes)):
        if minutes[j] - standard < usable:
            cnt += 1
        elif minutes[j] - standard == usable:
            cnt += 1
            break
        elif minutes[j] - standard > usable:
            cnt += 1
            break
    if ans[0] < cnt:
        ans[0] = cnt
        ans[1] = i+1

print(*ans)