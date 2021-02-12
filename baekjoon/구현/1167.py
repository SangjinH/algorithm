# https://www.acmicpc.net/problem/1167
import sys
input = sys.stdin.readline

n = int(input())

graph = [[]*(n+1)]

for _ in range(n):
    nums = list(map(int, input().split()))
    start = nums[0]
    print(start)
    nums = nums[1:]
    print(nums)
    while nums[0] != -1:
        graph[start].append((nums[0], nums[1]))
        nums = nums[2:]

