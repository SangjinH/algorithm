# https://www.acmicpc.net/problem/1977
import sys
input = sys.stdin.readline


m = int(input())
n = int(input())

i = 1
doubles = []

while True:

    if m <= i**2 <= n:
        doubles.append(i**2)

    i += 1

    if i**2 > n:
        break
if len(doubles) > 0:
    print(sum(doubles))
    print(doubles[0])
else:
    print(-1)