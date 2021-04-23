import sys
input = sys.stdin.readline

N = int(input())
colors = input().rstrip()

if colors[0] == 'R':
    standard = 'R'
else:
    standard = 'B'

colors = colors.split(standard)

cnt = 1
for i in colors:
    if i != '':
        cnt += 1

print(cnt)