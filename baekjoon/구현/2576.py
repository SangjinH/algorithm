# https://www.acmicpc.net/problem/2576
import sys
input = sys.stdin.readline

odds = []
for i in range(7):
    num = int(input().rstrip())
    if num % 2 == 1:
        odds.append(num)

odds.sort()

if len(odds) == 0:
    print(-1)
else:
    print(sum(odds))
    print(odds[0])
