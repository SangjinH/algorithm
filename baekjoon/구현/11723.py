# https://www.acmicpc.net/problem/11723
import sys
input = sys.stdin.readline

s = set()
n = int(input())

for _ in range(n):
    a = input().split()
    if a[0] == 'add':
        s.add(int(a[1]))
    elif a[0] == 'remove':
        if int(a[1]) in s:
            s.remove(int(a[1]))
    elif a[0] == 'check':
        if int(a[1]) in s:
            print(1)
        else:
            print(0)
    elif a[0] == 'toggle':
        if int(a[1]) in s:
            s.remove(int(a[1]))
        else:
            s.add(int(a[1]))
    elif a[0] == 'all':
        s = set(range(1,21))
    else:
        s = set()
