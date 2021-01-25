# https://www.acmicpc.net/problem/1449
# 백준 1449번 , 그리디, 수리공 항승
import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
troubles = list(map(int, input().rstrip().split()))
troubles.sort()

cnt = 0
tape = 0
for i in troubles:
    if tape <= i-0.5:
        tape = i-0.5



    while tape < i+0.5:
        cnt += 1
        tape += l

print(cnt)