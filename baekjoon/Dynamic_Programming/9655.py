import sys
input = sys.stdin.readline

N = int(input())

if (N % 4) in [1, 3]:
    print('SK')
else:
    print('CY')