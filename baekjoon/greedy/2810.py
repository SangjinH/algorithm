# https://www.acmicpc.net/problem/2810
import sys
input = sys.stdin.readline

n = int(input())
info = input().rstrip()

if info.count('LL') > 0:
    print(len(info.replace("LL","S"))+1)
else:
    print(n)