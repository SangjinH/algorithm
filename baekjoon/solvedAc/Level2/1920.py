import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
num_list = sorted(list(map(int, input().split())))

M = int(input())
check_list = deque(sorted(list(map(int, input().split()))))

print(num_list)
# print(check_list)
idx = 0
while 1:
    print(check_list)
    print(idx)
    if num_list[idx] == check_list[0]:
        check_list.popleft()
        print(1)
    elif num_list[idx] > check_list[0]:
        check_list.popleft()
        print(0)

    idx += 1

    if not check_list or idx == len(num_list):
