# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE
# 간단한 3, 6, 9 게임

import sys
input = sys.stdin.readline

n = int(input().rstrip())

nums = [ x for x in range(1, n+1)]
# print(nums)

counts = [0] * (n)
for i in range(len(nums)):
    if '3' in str(nums[i]):
        counts[i] += 1
    if '6' in str(nums[i]):
        counts[i] += 1
    if '9' in str(nums[i]):
        counts[i] += 1

for j in range(len(nums)):
    if counts[j] == 1:
        nums[j] = '-'
    elif counts[j] == 2:
        nums[j] = '--'
    elif counts[j] == 3:
        nums[j] = '---'

for i in nums:
    print(i, end=' ')

