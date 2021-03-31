import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    N = int(input())
    num_list = input()

    for i in p:
        if i == 'D':
            pass
        elif i == 'P':
