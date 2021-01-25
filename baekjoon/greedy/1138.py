# 한 줄로 서기
import sys
input = sys.stdin.readline

n = int(input().rstrip())
info = list(map(int, input().rstrip().split()))
position = [0 for _ in range(n)]

for i in range(n):
    cnt = 0
    num = info[i]   # 2
    for j in range(n):
        if num == cnt:
            position[i] = i+1
        else:
            if position[j] == 0:
                cnt += 1

print(position)