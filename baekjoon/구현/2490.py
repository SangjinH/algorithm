# 윷놀이, 백준 2490번
import sys
input = sys.stdin.readline

for _ in range(3):
    cnt = 0
    num_list = list(map(int, input().rstrip().split()))
    for i in range(len(num_list)):
        if num_list[i] == 0:
            cnt += 1
    if cnt == 0:
        print('E')
    elif cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')