import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
for _ in range(T):
    N = int(input())
    note1 = list(map(int, input().split()))
    check_dict = defaultdict(int)
    for i in note1:
        check_dict[i] = 1

    M = int(input())
    note2 = list(map(int, input().split()))
    for i in note2:
        if check_dict[i]:
            print(1)
        else:
            print(0)
