# https://www.acmicpc.net/problem/1676
import sys
from math import factorial

input = sys.stdin.readline

n = int(input())
num = str(factorial(n))[::-1]

cnt = 0
for i in num:
    if i == '0':
        cnt += 1
    else:
        print(cnt)
        break