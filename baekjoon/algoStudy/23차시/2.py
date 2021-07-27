# https://www.acmicpc.net/problem/2240

import sys
input = sys.stdin.readline

t, w = map(int, input().split())

arr = []

plum = ''

for i in range(t):
    temp = input().rstrip()
    if not plum:
        plum += temp
        print(plum)

    else:
        if plum[-1] != temp:
            arr.append(plum)
            plum = temp
        else:
            plum += temp

arr.append(plum)

print(arr)
