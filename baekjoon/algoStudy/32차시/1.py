import sys
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(float(input()))

for i in range(1, N):
    nums[i] = max(nums[i], nums[i]*nums[i-1])

print('{:.3f}'.format(max(nums)))