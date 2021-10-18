import sys
input = sys.stdin.readline

"""
단절점
단절선
"""

n = int(input())

tree = [i for i in range(2*n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

