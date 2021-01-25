# https://www.acmicpc.net/problem/1032
import sys
input = sys.stdin.readline

n = int(input())

paterns = []

for _ in range(n):
    paterns.append(input().rstrip())

bigyo = paterns[0]

paterns = paterns[1:]

results = []
for i in range(len(bigyo)):
    cnt = 0
    for j in range(len(paterns)):
        if bigyo[i] == paterns[j][i]:
           cnt += 1
    if cnt == n-1:
        results.append(bigyo[i])
    else:
        results.append('?')
res = ''
for i in results:
    res += i

print(res)