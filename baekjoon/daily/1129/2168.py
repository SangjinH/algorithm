import sys
input = sys.stdin.readline

x, y = map(int, input().split())

print(min(x, y)*2)
